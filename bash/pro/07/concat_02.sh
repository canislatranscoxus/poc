#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : string concatenation.                                    │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n String Concat 02 \n"

s1=; 
time for i in {1..10};
do 
    s1=${s1}${i}ant_;
    printf "%s %s \n" "s1: " "${s1}"

done;

s2=; 
time for i in {1..10};
do 
    s2+=${i}bee_;
    printf "%s %s \n" "s1: " "${s2}"
done