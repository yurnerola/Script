#!/usr/bin/expect -f
set ip [lindex $argv 0]
set password 5X2lSGr@B9iNS5fn!5rIcx,MG67.DE
set timeout 10
spawn ssh root@$ip
expect {
"*yes/no" {send "yes\r";exp_continue}
"*password:" {send "$password\r"}
}
interact
