#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: example using brace expansion                             │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n example 1: \n" 
s1=orange_{a..h..3}_strawberry
printf "%s \n" $s1

echo cat_{a..h..3}_dog