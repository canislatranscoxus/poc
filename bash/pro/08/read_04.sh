#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : read a file. Some verses from kjv bible.                 │
#│               Example 04.                                              │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Read file. Example 04. Some verses from bible. \n"

file_path="/home/art/git/poc/bash/pro/08/kjv_small.txt"

while IFS=: read  book chapter verse text ## read line ans store in vars
do
    first_word=${text%% *}
    printf "\n %s %s %s %s \n" "${book}" "${chapter}" "${verse}" "${first_word}"

done < $file_path


printf "\n End. \n" 

