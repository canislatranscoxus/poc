#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: # length of a string                                      │
#│                                                                        │
#│ Note: use return and exit to avoid closing the terminal                │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n type a password: "              
read passwd              
if [ ${#passwd} -lt 8 ]              
then              
  printf "Password is too short: %d characters\n" "${#passwd}" >&2           
  return 1   
  exit 1              
fi            