#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Loop example 03                                           │
#│              read data from array                                      │
#│ usage:                                                                 │
#│     ./loop_02.sh                                                       │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

IPs=("127.0.0.1" "192.168.2.1")
echo "IPs array: " ${IPs[@]}

for host_ip in ${IPs[@]}
do
    echo "IP: " $host_ip
    ping -c 2 $host_ip

done

