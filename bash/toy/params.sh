#┌────────────────────────────────────────────────────────────────────────┐
#│                                                                        │
#│ Description: This scripts read 3 parameters and print their values.    │
#│                                                                        │
#│ usage:                                                                 │
#│     ./params.sh cat dog fish                                           │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

echo "the name of this script is " $0
echo
echo "the value of parameter 1 is: " $1
echo
echo "the value of parameter 2 is: " $2
echo
echo "the value of parameter 3 is: " $3