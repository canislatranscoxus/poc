#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: array assign                                              │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Array assign \n "

printf "\n Example 1. Set all the values of an array in one command  \n"
states=( Arizona California  )
printf "\n states: \n"
printf "%s\n"  "${states[@]}"


printf "\n Example 2. Add one item at the end of the array \n"
states+=( Florida )
printf "%s\n"  "${states[@]}"

printf "\n Example 3. Add many items at the end of the array \n"
states+=( Massachusetts Utah Texas Virginia)
printf "%s\n"  "${states[@]}"
