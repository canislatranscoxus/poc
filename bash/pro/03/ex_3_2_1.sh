#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Exercise 3.2 :                                                         │
#│                                                                        │
#│ Write a script that prompts the user to enter the name of a file.      │
#│ Repeat until the user enters a file that exists.                       │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


while true
do

    printf "write the name of a file: "
    read file_name

    printf "%s %s \n" "your file: " $file_name

    if test -e $file_name
    then
        printf "your file exist, cool ! \n" 
        break

    else
        printf "file does not exist, buuu \n" 
    fi
    
done
