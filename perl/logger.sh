#!/bin/bash
cd /data0/ChatServer11020/UCChatHall_log;
for i in `ls -t|grep 455135`;do echo $i;cat $i|grep use_prop|grep 100000172;done
