#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: uppercase                                                 │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Uppercase \n "

book="one thousand and one nights"

printf "%s %s \n" "my bookis : " "${book}"

printf "%s \n" "${book^}"
printf "%s \n" "${book^^}"

printf "\n Uppercase first letter found from m to z: \n"
printf "%s \n" "${book^[m-z]}"
printf "\n Uppercase all letter found from m to z: \n"
printf "%s \n" "${book^^[m-z]}"


