#!/bin/bash
cd /data0/ChatServer/UCChatHall_log;
for i in `ls -t|grep 475882`;do echo $i;cat $i|grep use_prop|grep 100000172;done
