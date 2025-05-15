#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: array assign                                              │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Array assign \n "

printf "\n Example 1  \n"
name[0]=Daisy
name[5]="Rapunzel"

printf "%s %s \n"  "name 0: " "${name[0]}"
printf "%s %s \n"  "name 5: " "${name[5]}"


printf "\n Example 2. Array with 4 random numbers  \n"

unset a              
a[${#a[@]}]="1 $RANDOM" ## ${#a[@]} is 0              
a[${#a[@]}]="2 $RANDOM" ## ${#a[@]} is 1              
a[${#a[@]}]="3 $RANDOM" ## ${#a[@]} is 2              
a[${#a[@]}]="4 $RANDOM" ## ${#a[@]} is 3              
printf "%s\n" "${a[@]}" 
