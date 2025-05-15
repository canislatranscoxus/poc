#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Compare two strings, no case sensitive.                  │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Compare two strings without regard of case. Example 01. \n"
printf "\n Strategy: we convert to uppercase both strings and compare. \n"

s1="the scarlet dress"; 
s2="the scarlet dress";

printf "\n  %s %s \n" "s1: " "${s1}"
printf "\n  %s %s \n" "s2: " "${s2}"


s1=`echo $s1 | tr [a-z] [A-Z]`
s2=`echo $s2 | tr [a-z] [A-Z]`



printf "\n  %s %s \n" "result: " "${result}"