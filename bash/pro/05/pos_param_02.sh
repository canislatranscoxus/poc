#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Positional parameters. Example 2. shift                   │
#│                                                                        │
#│ Usage      :                                                           │
#│             . pos_param_02.sh a b c d e f g h i j k                    │                                                                       
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Positional Parameters. Example 2. \n "
printf "%s %s \n" ": "params: "${@}" 



printf "%s %s \n" "shift 2: " 
shift 2
txt="${@}"
printf "%s %s \n" "after shift 2: " "${txt}" 

printf "%s %s \n" "shift (( # - 3 )). Remove but the last 3 params " 
shift "$(( $# - 3 ))"
printf "%s %s \n" "after shift (( # - 3 )): " "${@}" 



printf "%s %s \n" "shift #. Remove all the prameters.: " 
shift "${#}"
printf "%s %s \n" "params: " "${@}" 
