#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: For loop example 01                                       │
#│              print integer numbers from 0 to 5.                        │
#│ usage:                                                                 │
#│     ./loop_01.sh                                                       │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

for (( i=0; i<=5; i++ ))
do
    echo $i
done

