#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: display error message if empty or unset                   │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "arguments \n "

printf "%s \n" $1
printf "%s \n" $2



printf "\n\n display error message 01.  \n"

printf "check for empty or unset \n "
echo ${1:?arg 1 is required.}
echo ${2:?arg 2 is required.}

printf "\n check for unset \n "
echo ${1?arg 1 is unset.}
echo ${2?arg 2 is unset.}
