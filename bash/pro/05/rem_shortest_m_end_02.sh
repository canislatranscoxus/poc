#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: remove shortest match from the end of the string          │
#│              example 2;                                                │
#│              remove the last / and file name from a path,              │
#|              to extract the directory                                  │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "remove shortest match from the end of the string\n "

my_path=/home/donald/duck/prog/my_script.py

dir=${my_path%/*}

printf "%s %s \n" "path: " $my_path
printf "%s %s \n" "my dir is: " $dir

