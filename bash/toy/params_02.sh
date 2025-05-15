#┌────────────────────────────────────────────────────────────────────────┐
#│                                                                        │
#│ Description: This scripts read 2 parameters and print their values.    │
#│                                                                        │
#│ usage:                                                                 │
#│     ./params_02.sh -h my_crazy_laptop -o ping                          │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

echo "Help. Run the script like this:"
echo "parameters:"
echo "-h    Host name"
echo "-o    Operation"
echo "example: "
echo  "     ./params_02.sh -h my_computer -o ping "

while getopts ":h:o:" option
# the leading colon in the option list suppreses displaying error messages
# when unknown options are passed
do 
    case ${option} in
        h ) echo "host name: " $OPTARG ;;
        o ) echo "operation: " $OPTARG ;;
        * ) echo "please, provide correct parameters"
    
    esac
done
