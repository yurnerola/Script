#!/bin/bash
cd /data0/ChatServer22167/UCChatHall_log;
for i in `ls -t|grep 430892`;do echo $i;cat $i|grep use_prop|grep 100000172;done
