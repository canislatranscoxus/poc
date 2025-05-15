#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: example using parameter expansion                         │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n example 1, printf param expansion: \n" 
p1=strawberry
printf "%s \n" "I like the $p1"

printf "\n example 2, echo param expansion: \n" 
echo "I bite the $p1"