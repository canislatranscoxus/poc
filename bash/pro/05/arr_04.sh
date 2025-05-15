#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Associative Arrays                                        │
#│              for each                                                  │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Associative Array \n "

printf "\n Example 1. Set all the values of an array in one command  \n"
fruits=( apple banana orange grape "blue berry"  )

printf "\n my fruits are: \n"

for i in ${fruits[@]}
do
    printf "%s \n" $i
done

printf "\n"