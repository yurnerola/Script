//判断如果为占麦狗或者转播员，则不分发聊天内容
if(isFakeUser(lstUcClCrsDataId.mi64DstUserID)) 
	return false;

//如果是游客且不再产品白名单中，则不分发聊天内容
if (moVistorIDManager.IsVisitor(apUserInfo->mi64UserId) && 
	moVisitorTextAllowedPidList.find(apUserInfo->mlUserState>>24)==moVisitorTextAllowedPidList.end())
	return false;

char lcSendBuf[ DEFMAXTCPBUFFLEN +1] = {0} ; 
int	liPackLength = 0;
liPackLength = lstUcClCrsDataId.Pack(lcSendBuf,DEFMAXTCPBUFFLEN) ;

//如果用户处在禁言状态，不分发消息内容
if (apUserInfo->GetUserState(CHATROOM_USER_NOSPEAK_STATE) )
{
	TRACE(5,"CChatHall::Deal_CL_CRS_DATA_ID_350_EX 用户" << lstUcClCrsDataId.mi64SrcUserID << "处于禁言状态丢弃数据包!" );
	return false;
}
//判断包中的ID与登录时的ID是否一致
if (apUserInfo->mi64UserId != lstUcClCrsDataId.mi64SrcUserID)
{
	//用户发送的非法数据包
	TRACE(1,"CChatHall::Deal_CL_CRS_DATA_ID_350_EX 非法的聊天消息,用户:" << apUserInfo->mi64UserId 
		<< " 地址:" << inet_ntoa(*(in_addr*)(&apUserInfo->mulPeerIpAddr)));
	return false;
}

STRU_UC_CL_CRS_USER_MESSAGE lstruUserMessage;
//数据的长度提前加进去
lstruUserMessage.mwMessageLen = lstUcClCrsDataId.mwDataLen;
if(lstruUserMessage.UnPack(lstUcClCrsDataId.mData, lstUcClCrsDataId.mwDataLen) != 1)
{
	//解包错误
	TRACE(2,"CChatHall::Deal_CL_CRS_DATA_ID_350_EX 非法的聊天消息,用户:" << apUserInfo->mi64UserId 
		<< " 地址:" << inet_ntoa(*(in_addr*)(&apUserInfo->mulPeerIpAddr)));
	return false;
}
//又一次判断，有点存储信息冗余
if(isFakeUser(lstruUserMessage.mi64ToUserID))
	return false;

//判断消息包长度
if (lstruUserMessage.mwMessageLen >= 310 || lstruUserMessage.mwMessageLen == 0)
{
	TRACE(5,"CChatHall::Deal_CL_CRS_DATA_ID_350_EX 用户:" << lstUcClCrsDataId.mi64SrcUserID << "非法的消息包长度!"
		<<" mwMessageLen:"<<lstruUserMessage.mwMessageLen);
	return false;
}

//只允许通过类型为0、2、3、11的包
if(	lstruUserMessage.mbyType == 1 ||									//过滤掉为1的
	(lstruUserMessage.mbyType > 3 && lstruUserMessage.mbyType != 11) )	//过滤掉大于3不为11的
{
	TRACE(5,"CChatHall::Deal_CL_CRS_DATA_ID_350_EX 非法的聊天消息,用户:" << apUserInfo->mi64UserId
		<< " IP地址:" <<  CCommon::GetIPAddr(apUserInfo->mulPeerIpAddr)
		<< " 类型:" << lstruUserMessage.mbyType);
	return false;
}

char lszTemp1 = '<';
char lszTemp2 = '>';
if (strchr(lstruUserMessage.macMood, lszTemp1) != NULL || strchr(lstruUserMessage.macMood, lszTemp2) != NULL)
{
	TRACE(1, "CChatHall::Deal_CL_CRS_DATA_ID_350_EX 用户ID:" << lstUcClCrsDataId.mi64SrcUserID
		<< " 进行网页攻击:" << lstruUserMessage.macMood);
	return false;
}
//防止普通用户篡改心情
std::string lstrmacMood = lstruUserMessage.macMood;
string::size_type loc = lstrmacMood.find( "%1", 0 );

if(loc == string::npos )
{
	//非管理员心情字段一定要带%1，以显示发送信息人的用户ID
	if(apUserInfo->mbyGrade == DEF_MANAGER_POWER_USER)
	{
		TRACE(1, "CChatHall::Deal_CL_CRS_DATA_ID_350_EX 用户ID:" << lstUcClCrsDataId.mi64SrcUserID
			<< " 篡改心情字段:" << lstruUserMessage.macMood);
		return false;
	}
	else
	{
		//temp: 非法数据包
		//管理员心情字段如果没带%1，记录它
		TRACE(1, "CChatHall::Deal_CL_CRS_DATA_ID_350_EX 用户ID:" << lstUcClCrsDataId.mi64SrcUserID
			<< " 篡改心情字段:" << lstruUserMessage.macMood << " 信息内容：" << lstruUserMessage.macMessage);
	}
}

TRACE(5, "CChatHall::Deal_CL_CRS_DATA_ID_350_EX RecvBufLen:" << aiRecvBufLen
	<< " 源用户ID:" << apUserInfo->mi64UserId << " 类型:" << lstruUserMessage.mbyType
	<< " 目的用户ID:" << lstUcClCrsDataId.mi64DstUserID);


bool dstFinded = false;
STRU_HALL_USER_INFO lstruHallUserInfo;
if (lstUcClCrsDataId.mi64DstUserID != 0)
{
	dstFinded = moUserList.LookupHallUser(lstUcClCrsDataId.mi64DstUserID, lstruHallUserInfo);
	if ((apUserInfo->miRoomId!=0 && apUserInfo->miRoomId!=(uint32_t)mpUCHall->mlHallID) || !dstFinded)
	{
		return dealWatchPrivateChatReq(lstUcClCrsDataId,lstruUserMessage,apUserInfo);
	}
}
	
//检查用户是否需要输入聊天验证码
if((lstruUserMessage.mbyType == 2 || lstruUserMessage.mbyType == 0)
	&& IsNeedInputChatCode(apUserInfo,lstruUserMessage.mi64ToUserID,lstruUserMessage.macMessage))
{
	return true;
}

if(lstUcClCrsDataId.mi64DstUserID || lstruUserMessage.mbyType == 2)
{
	//判断用户的在线时长
	if(apUserInfo->miOnlineTime < mpUCHall->miPrivateChatTimeThreshold)
	{
		TRACE(5, "CChatHall::Deal_CL_CRS_DATA_ID_350_EX 用户:" << lstUcClCrsDataId.mi64SrcUserID 
			<< "在线时长:" << apUserInfo->miOnlineTime << "不足，不能实行私聊!");

		char lszSendBuf[128] = "";
		sprintf(lszSendBuf, " 您还未达到规定的在线时长，暂时不能私聊。");
		InformUser(apUserInfo, lszSendBuf);
		return false;
	}


	//if (moUserList.LookupHallUser(lstUcClCrsDataId.mi64DstUserID, lstruHallUserInfo))
	if (dstFinded && (lstruHallUserInfo.miRebroadHallId == mpUCHall->mlHallID))
	{

		//判断用户的在线时长
		if(apUserInfo->miOnlineTime < mpUCHall->miPrivateChatTimeThreshold)
		{
			TRACE(5, "CChatHall::Deal_CL_CRS_DATA_ID_350_EX 用户:" << lstUcClCrsDataId.mi64SrcUserID 
				<< "在线时长:" << apUserInfo->miOnlineTime << "不足，不能实行私聊!");

			char lszSendBuf[128] = "";
			sprintf(lszSendBuf, " 您还未达到规定的在线时长，暂时不能私聊。");
			InformUser(apUserInfo, lszSendBuf);
			return false;
		}

		if (liPackLength > 0)
		{
			if (1 != lstruHallUserInfo.mi64UserId && lstruHallUserInfo.GetUserState(CHATROOM_USER_RECV_PRIVATE_TALK))
            {
				moChatMessageFilter.addTask(lstruHallUserInfo.mlHashMapKey,lstruHallUserInfo.mhIoSocket,
					lstruUserMessage.macMessage,lstruUserMessage.mwMessageLen,lcSendBuf,liPackLength);
			}
		}
		else
		{
			TRACE(1,"CChatHall::Deal_CL_CRS_DATA_ID_350_EX 2 打包失败.");
			return false;
		}
	}

	if (mpUCHall->mbIsRecordMessage)
	{
		//记录私聊信息
		moMsgRec.AddMessage(CMessageRecord::PRIVATE_MESSAGE,
			apUserInfo->mi64UserId,
			lstruUserMessage.mi64ToUserID,
			apUserInfo->macNickName,
			apUserInfo->mulPeerIpAddr,
			lstUcClCrsDataId.mData,
			lstUcClCrsDataId.mwDataLen);
	}
