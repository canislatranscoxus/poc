#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Exercise 3.1 :                                                         │
#│                                                                        │
#│ Write a script that asks the user to enter a number between 20 and 30. │
#│ If the user enters an invalid number or a non-number, ask again.       │
#│ Repeat until a satisfactory number is entered.                         │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

# flag to keep working
flag_ok=0

until [ $flag_ok -eq 1 ]
do
    is_num=0

    printf "Enter a number between 20 and 30 (inclusive): "
    read number


    case $number in
        *[!0-9]*) is_num=0 ;;
        *) is_num=1 ;;
    esac

    printf "%s ---%s--- \n" "is_num:" $is_num
    printf "%s %s \n" "number:" $number

    printf "\n\n is_num = 0 ? \n\n"

    if [ $is_num -eq 0 ]
    then
        printf "this is NOT a valid number \n " 
        flag_ok=0
    elif (( number < 20 || number > 30 ))
    then
        printf "this num is out of range \n"
        flag_ok=0
    else
        printf "Good number  \n " 
        flag_ok=1
    fi

    printf "%s %s \n" "flag_ok: " $flag_ok

done

printf "\n bye \n"