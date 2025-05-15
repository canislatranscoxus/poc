#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: extract substring                                         │
#│              var:offset:length                                         │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Substring, example 2. \n "

txt="We like cats and dogs"
printf "%s %s \n" "txt: " "$txt"
printf "%s %s \n" "substring -4: " "${txt: -4}"
printf "%s %s \n" "substring 6: -4: " "${txt:6: -4}"

printf "\n\n"

txt="We_like_cats_and_dogs"
printf "%s %s \n" "txt: " "$txt"
printf "%s %s \n" "substring -4: " "${txt: -4}"
printf "%s %s \n" "substring 0: -4: " "${txt:0: -4}"

