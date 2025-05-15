#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Exercise 3.2 :                                                         │
#│                                                                        │
#│ Write a script that prompts the user to enter the name of a file.      │
#│ Repeat until the user enters a file that exists.                       │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

# flag to keep working
file_exist="n"


while [ $file_exist = "n" ]
do

    printf "write the name of a file: "
    read file_name

    printf "%s %s \n" "your file: " $file_name

    if test -e $file_name
    then
        file_exist="y"
        printf "your file exist, cool ! \n" 

    else
        file_exist="n"
        printf "file does not exist, buuu \n" 
    fi

    
done
