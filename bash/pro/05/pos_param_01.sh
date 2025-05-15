#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Positional parameters                                     │
#│                                                                        │
#│ Usage      :                                                           │
#│             . pos_param_01.sh a b c d e f g h i j k                    │                                                                       
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "arguments \n "

printf "%s %s \n" "param 1: " $1
printf "%s %s \n" "param 2: " $2
printf "%s %s \n" "param 3: " ${3}

printf "to use a positional parameter with index 10 or bigger use braces always {} \n"
printf "%s %s \n\n" "param 10: " ${10}


txt="${@}"
printf "%s %s \n\n" "@ll params: " "${txt}"

printf "%s %s \n" "*ll params: " "${*}"

printf "\n\n"