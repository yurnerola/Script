#!/bin/bash
cd /data0/ChatServer11112/UCChatHall_log;
for i in `ls -t|grep 447283`;do echo $i;cat $i|grep use_prop|grep 100000172;done
