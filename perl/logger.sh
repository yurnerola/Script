#!/bin/bash
cd /data0/ChatServer22025/UCChatHall_log;
for i in `ls -t|grep 472559`;do echo $i;cat $i|grep use_prop|grep 100000172;done
