#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: example using arithmetic expansion                        │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n example 1: 4 * 16 \n" 
s1=$((4 * 16))
printf "%s \n" $s1

x=10
printf "\n x = 10 \n"

printf "\n example 2: --x \n" 
s1=$(( --x ))
printf "%s \n" $s1

printf "\n example 3: x++ \n" 
s1=$(( x++ ))
printf "%s \n" $s1

printf "\n example 4: x \n" 
s1=$(( x ))
printf "%s \n" $s1

printf "\n x = 10 \n"
printf "\n example 5: x < 10 ? 100 : 200 \n" 
s1=$(( x < 10 ? 100 : 200 ))
printf "%s \n" $s1
