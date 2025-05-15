#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : string concatenation.                                    │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

animal1=cats
animal2="dogs"
s1=""
s1=${animal1}" and "${animal2}

printf "%s %s \n" "s1: " "${s1}"

s2=""
s2+="we love "
s2+=${animal1}
s2+=" and "
s2+=${animal2}
printf "%s %s \n" "s2: " "${s2}"


