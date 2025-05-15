#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Convert to upper case.                                   │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Convert case, upper lower. Example 02. \n"

s1="the scarlet woman was wearing a necklace"; 

printf "\n  %s %s \n" "s1: " "${s1}"

echo $s1 | tr [a-z] [A-Z]

result=`echo $s1 | tr [a-z] [A-Z]`

printf "\n  %s %s \n" "result: " "${result}"