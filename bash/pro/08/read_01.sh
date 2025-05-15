#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : read a file.                                             │
#│               Example 01.                                              │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Read file. Example 01. \n"

file_path="/home/art/git/poc/bash/pro/08/contact.txt"

while read      ## no name supplied, so variable REPLY will be used
do
    printf "\n %s \n" "${REPLY}"

done < $file_path


printf "\n End. \n" 

