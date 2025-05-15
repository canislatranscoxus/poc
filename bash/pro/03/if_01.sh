#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: small script using if command                             │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

name=Merida

if [ -z $name ]
then
    printf "%s \n" "the variable name is empty"
else
    printf "%s %s \n" "her name is " $name
fi