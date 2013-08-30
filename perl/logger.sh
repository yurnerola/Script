#!/bin/bash
cd /data0/ChatServer11014/UCChatHall_log;
for i in `ls -t|grep 1991`;do echo $i;cat $i|grep use_prop|grep 100000172;done
