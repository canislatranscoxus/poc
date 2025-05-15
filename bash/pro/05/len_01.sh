#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: # length of a string                                      │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

animal=crocodile

printf "# length of a string \n "

printf "%s %s \n" "animal=" $animal

printf "%s %s %s \n" "the length of animal is: " ${#animal} " characters"

