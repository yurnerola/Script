#!/bin/bash
cd /data0/ChatServer22216/UCChatHall_log;
for i in `ls -t|grep 452720`;do echo $i;cat $i|grep use_prop|grep 100000172;done
