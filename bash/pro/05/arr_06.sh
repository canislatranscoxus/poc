#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: split string and output Array                             │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘


text="Tae Kwon Do,Box,Wrestling,Judo,Jiu Jitsu,Muay Thai"

IFS=',' read -ra ids <<< "$text"

for i in "${ids[@]}"
do
echo "$i"
done
