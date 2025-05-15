#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : string concatenation.                                    │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Repeat until string length is less  than 20 \n"

s1=; 
max_len=20

while (( ${#s1} < ${max_len} ))
do 
    s1=${s1}ant_;
    printf "%s %s \n" "s1: " "${s1}"

done;

printf "\n %s %s chars \n" "s1 len is : " ${#s1}

