#!/bin/bash
cd /data0/ChatServer22130/UCChatHall_log;
for i in `ls -t|grep 419888`;do echo $i;cat $i|grep use_prop|grep 100000172;done
