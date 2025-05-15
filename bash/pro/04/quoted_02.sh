#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: example using quotes                                      │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n example 1: \n" 
s1="cat \n dog \n fish \n turtle \n bunny \n"
printf "%b \n" $s1

s1="apple \n banana \n orange  \n lemon \n"
printf "%b %b \n" "example 2: " $s1


printf "\n example 3: \n" 
printf 'apple \n banana \n orange  \n lemon \n pineapple \n melon \n strawberry \n blue_berry \n'
