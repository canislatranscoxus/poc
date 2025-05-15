#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: array display                                             │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Array display \n "

printf "\n Example 1 @ quoted \n" 
printf "%s\n"  "${BASH_VERSINFO[@]}"

printf "\n Example 2 @ unquoted \n" 
printf "%s\n"  ${BASH_VERSINFO[@]}


printf "\n Example 3 * quoted ( all the elements in one line ) \n" 
printf "%s\n"  "${BASH_VERSINFO[*]}"

printf "\n Example 4 * unquoted \n" 
printf "%s\n"  ${BASH_VERSINFO[*]}

printf "\n Example 5. slicing, from element index 1 to 3 \n" 
printf "%s\n"  "${BASH_VERSINFO[@]:1:3}"

printf "\n Example 6. length of array \n" 
printf "%s\n"  "${#BASH_VERSINFO[*]}"
printf "%s\n"  "${#BASH_VERSINFO[@]}"

printf "\n Example 6. length of element with index 4 \n" 
printf "%s %s\n"  "element 4: "  "${BASH_VERSINFO[4]}"
printf "%s %s\n"  "length   : "  "${#BASH_VERSINFO[4]}"