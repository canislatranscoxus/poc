#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Positional parameters. Example 3. shift                   │
#│                                                                        │
#│ Usage      :                                                           │
#│             . pos_param_03.sh ant bee cat                              │                                                                       
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Positional Parameters. Example 3. \n "
printf "%s %s \n" ": "params: "${@}" 


printf "\n for loop  \n"

# both lines are ok
#for param 
#for param in ${@}

for param in ${@}
do
    printf "%s %s \n" "param: " $param 
done

printf "\n while loop  \n"
while (( $# ))
do
    printf "%s %s \n" "param: " $1 
    shift
done
