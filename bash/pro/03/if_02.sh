#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: small script using if command                             │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Enter a number less or equal than 10: "
read number

if (( number <= 10 ))
then
    printf "%s %d \n" "I like number " $number
else
    printf "\n your number is too big \n" 
fi