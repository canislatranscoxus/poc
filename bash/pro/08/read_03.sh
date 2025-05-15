#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : read a file. Some verses from kjv bible.                 │
#│               Example 03.                                              │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Read file. Example 03. Some verses from bible. \n"

file_path="/home/art/git/poc/bash/pro/08/kjv_small.txt"

while IFS=: read  book chapter verse text ## read line ans store in vars
do
    printf "\n book= %s  ch= %s verse= %s \n" "${book}" "${chapter}" "${verse}"

done < $file_path


printf "\n End. \n" 

