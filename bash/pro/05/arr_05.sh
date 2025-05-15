#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Associative Arrays                                        │
#│              for each                                                  │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Associative Array \n "

unset fruits
declare -A fruits=( [a]="apple" [b]="banana" [c]="cherry" [sb]="straw berry" )


printf "\n my fruits are: \n"

#printf "%s %s \n" "a:" ${fruits["a"]}
printf "%s  \n" "${fruits[@]}"
printf "\n"

printf "%s %s \n" "a : " "${fruits[a]}"
printf "%s %s \n" "b : " "${fruits[b]}"
printf "%s %s \n" "c : " "${fruits[c]}"
printf "%s %s \n" "sb: " "${fruits[sb]}"

printf "\n"