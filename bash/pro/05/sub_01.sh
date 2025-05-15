#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: extract substring                                         │
#│              var:offset:length                                         │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Substring, example 1. \n "

txt="We like cats and dogs"

printf "%s %s \n" "txt: " "$txt"

printf "%s %s \n" "substring 0 4: " "${txt:0:4}"
printf "%s %s \n" "substring 1 4: " "${txt:1:4}"
printf "%s %s \n" "substring 2 4: " "${txt:2:4}"
printf "%s %s \n" "substring 3 4: " "${txt:3:4}"

printf "%s %s \n" "substring 2 : " "${txt:2}"
