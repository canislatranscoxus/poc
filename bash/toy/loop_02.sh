#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Loop example 02                                           │
#│              Print pair numbers from 10 to 10, incrementing by 2       │
#│ usage:                                                                 │
#│     ./loop_02.sh                                                       │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

for i in {10..20..2}
do
    echo $i
done

