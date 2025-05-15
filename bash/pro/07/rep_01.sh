#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : string concatenation.                                    │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Repeat until string length is less  02 \n"

s1=; 
time for i in {1..10};
do 
    s1=${s1}${i}ant_;
    printf "%s %s \n" "s1: " "${s1}"

done;
