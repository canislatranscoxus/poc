#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: While loop example 01                                     │
#│              read data from array                                      │
#│ usage:                                                                 │
#│     ./while_01.sh                                                      │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

i=0

while [ $i -le 5 ]
do
    echo "i: " $i
    i=$(( $i + 1 ))
done

