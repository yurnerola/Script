import tornado.ioloop
import tornado.web
import pymongo
import time
import datetime

mgconn=pymongo.Connection('10.10.10.64', 35000)
mgcur=mgconn['web_login_cache']

class updateHandler(tornado.web.RequestHandler):
    def post(self):
        isflag = True
        dic = {}
        dic = eval(self.request.body)
        hallid = dic.get('hall_id')
        if (hallid != None):
            mgcoll=mgcur['web_hall_list']
            result = mgcoll.find_one({"_id":long(hallid)})
            if (result == None): 
                self.write('succ')
                return ''
        
        type = dic.get("type")
        #print(type+' '+str(hallid))
        if type == 'user_list':
            self.update_user_list(dic,hallid)
            self.write("succ")
        elif type == 'mic_list':
            self.update_mic_list(dic,hallid)
            self.write("succ")
        elif type == 'chat':
            self.update_chat(dic, hallid)
            self.write("succ")
        elif type == 'runway':
            self.write("succ")
        elif type == 'runway_2':
            self.update_runway_2(dic, hallid)
            self.write("succ")
        elif type == 'speaker':
            self.write("succ")
        elif type == 'speaker_2':
            self.update_speaker_2(dic, hallid)
            self.write('succ')
        elif type == 'user_info':
            self.write("succ")
        elif type == 'user_info_2':
            self.update_user_info_2(dic)
            self.write("succ")
        elif type == 'hall_topic':
            self.update_hall_topic(dic, hallid)
            self.write("succ");
        else:
            self.write("request json type error")

    def update_user_info_2(self, request):
                user = request.get('user_info')
                if (user != None):
                        mgcoll=mgcur['user_info']
                        #print(user)
                        mgcoll.save(user)
                        
    def update_speaker_2(self, request, hallid):
            speaker = request.get('speaker')
            if (speaker != None):
                    mgcoll=mgcur['hall_info']
                    mgcoll.update({'_id':long(hallid)}, {'$set':{"speaker":speaker}})
                
    def update_hall_topic(self, request, hallid):
            hall_topic = request.get('hall_topic')
            if (hall_topic != None):
                mgcoll=mgcur['hall_info']
                mgcoll.update({'_id':long(hallid)}, {'$set':{"hall_topic":hall_topic}})        
                        
    def update_runway_2(self, request, hallid):
            runway = request.get('runway')
            if (runway != None):
                mgcoll=mgcur['hall_info']
                mgcoll.update({'_id':long(hallid)}, {'$set':{"runway":runway}})
                        
    def update_chat(self, request, hallid):
        chat = request.get('chat')
        from_id = chat.get('from_id')
        if (chat != None):
            usrcoll = mgcur['user_info']
            from_user = usrcoll.find_one({'_id':long(from_id)})
            if (from_user != None):
                chat['from_nick'] = from_user.get('user_nick')
                chat['power'] = from_user.get('power')
                chat['service_type'] = from_user.get('service_type')
                chat['vip_level'] = from_user.get('vip_level')
                chat['photo_num'] = from_user.get('photo_num')                             
            dt = time.localtime()

        chat['time'] = str(dt.tm_hour)+":"+str(dt.tm_min)+":"+str(dt.tm_sec)
        mgcoll = mgcur['hall_info']
        mgcoll.update({"_id":hallid}, {"$push":{"chat_list":chat}, "$inc":{"chats_size":1}})
        mgcoll.update({"_id":hallid, "chats_size":{"$gt":10}}, {"$pop":{"chat_list":-1}, "$inc":{"chats_size":-1}})


    '''
    curl -d "{\"type\":\"user_list\",\"hall_id\":456034,\"usr_cnt\":3,\"uid_list\":[10622,8001,8002]}" http://localhost:18888/update_cache.js    
    '''
    def update_user_list(self,request,hallid):
        if(request.get('uid_list'),[]):
            user_info=mgcur['user_info']
            id_list=request.get('uid_list')
            cursor=user_info.find({"_id":{"$in":id_list}})
            user_list_sort=[]
            user_list=[]
            for user in cursor:
                user_list_sort.append(user)

            for id in id_list:
                for user in user_list_sort:
                    if(id==user["_id"]):
                        user_list.append(user)
                        break;
            hall_info=mgcur['hall_info']
            hall_info.update({"_id":request["hall_id"]},{"$set":{"user_list":user_list,"usr_cnt":request["usr_cnt"]}},upsert=True, safe=True)


    def update_mic_list(self,request,hallid):
        if(request.get('uid_list'),[]):
            user_info=mgcur['user_info']
            id_list=request.get('uid_list')
            cursor=user_info.find({"_id":{"$in":id_list}})
            user_list_sort=[]
            user_list=[]
            for user in cursor:
                user_list_sort.append(user)

            for id in id_list:
                for user in user_list_sort:
                    if(id==user["_id"]):
                        user_list.append(user)
                        break;
            hall_info=mgcur['hall_info']
            hall_info.update({"_id":request["hall_id"]},{"$set":{"mic_list":user_list}},upsert=True, safe=True)



application = tornado.web.Application([
    (r"/update_cache.js", updateHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()