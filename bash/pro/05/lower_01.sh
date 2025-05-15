#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: lowercase                                                 │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "lowercase \n "

book="THE HOUND OF THE BASKERVILLES"

printf "%s %s \n" "my bookis : " "${book}"

printf "%s \n" "${book,}"
printf "%s \n" "${book,,}"

printf "\n lowercase first letter found from m to z: \n"
printf "%s \n" "${book,[M-Z]}"
printf "\n lowercase all letter found from m to z: \n"
printf "%s \n" "${book,,[M-Z]}"


