#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : string concatenation.                                    │
#│                                                                        │
#│ Usage:                                                                 │
#│        repeat string num_of_times                                      │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Repeat until string length is less  than 20 \n"

repeat()
{

str="${1}" 
num_of_times=$2
s=;
i=0

printf "%s %s \n" "str: " ${str}
printf "%s %s \n" "num_of_times: " ${num_of_times} 
printf "%s %s \n" "s: " ${s} 
printf "%s %s \n" "" "" i=0



for ((i=1; i <= $num_of_times; i++));
do 
    
    s=${s}"${str}";
    printf "%s %s \n" ${i} "${s}"

done;

printf "\n %s %s chars \n" "s len is : " ${#s}

}

