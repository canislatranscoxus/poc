#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Convert to lower case.                                   │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Convert to lower case. Example 03. \n"

s1="THE HOUND OF THE BASKERVILLES"; 

printf "\n  %s %s \n" "s1: " "${s1}"

echo $s1 | tr [A-Z] [a-z] 

result=`echo $s1 | tr [A-Z] [a-z]`

printf "\n  %s %s \n" "result: " "${result}"