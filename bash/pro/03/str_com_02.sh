#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: test lexicographic positions of strings.                  │
#│              test, the alphabetical order of the strings,              │
#│              just like in the dictionary.                              │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

s1="anastasia"
s2="elsa"

printf "%s \n" "Test lexicographic positions of strings"

printf "%s %s \n" "s1: " $s1
printf "%s %s \n" "s2: " $s2

printf "%s \n" "s1 is previous s2 ? " 
[ $s1 \< $s2 ]
printf "%s \n\n" $?

printf "\n\n"
printf "%s \n" "s2 is previous s1 ? " 
[ $s2 \< $s1 ]
printf "%s \n\n" $?