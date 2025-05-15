#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: small script using if command                             │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Enter a number between 10 and 20 (inclusive): "
read number

if [ $number -lt 10 ]
then
    printf "this is very small \n"
elif [ $number -gt 20 ]
then    
    printf "wow! the number is too big \n" 
else
    printf "%s %s \n" "your lucky number is " $number 
fi