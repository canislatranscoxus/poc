#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Convert case, upper lower.                               │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Convert case, upper lower. Example 01. \n"

printf "\n replacing chars tsw by TSW \n"


s1="the scarlet woman was wearing a necklace"; 

printf "\n  %s %s \n" "s1: " "${s1}"

echo $s1 | tr tsw TSW

result=`echo $s1 | tr tsw TSW`

printf "\n  %s %s \n" "result: " "${result}"