#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: example using command expansion or                        │
#│              backticks ``                                              │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n example 1:  \n" 
s1=$( date )
printf "%s " $s1

printf "\n\n example 2:  \n" 
s1=` date `
printf "%s " $s1

printf "\n \n"

