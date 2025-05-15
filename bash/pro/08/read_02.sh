#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : read a file.                                             │
#│               Example 02.                                              │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Read file. Example 02. \n"

file_path="/home/art/git/poc/bash/pro/08/contact.txt"

while read  name phone  ## we store the fisrt word in name, and the second in phone
do
    printf "\n %s %s \n" "${name}" "${phone}"

done < $file_path


printf "\n End. \n" 

