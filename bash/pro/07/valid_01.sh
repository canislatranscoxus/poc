#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Check is if it is a valid variable name.                 │
#│               Call function ans store result in a variable.            │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Valid variable name. Example 01. \n"


name1="the %  scarlet + wom@n"; 
name2="123street"; 
name3="address"; 

is_valid_name()
{
    var_name=$@
    result=1

    case $var_name in
        # it does not start with letter or underscore
        # or contain a char that is not letter, number or underscore, 
        # it is NOt Valid name
        [!a-zA-Z_]* | *[!a-zA-Z0-9_]* ) result=0 ;;
    esac

    #printf "\n %s %s \n" "var_name: " "${var_name}"
    #printf "\n %s %s \n" "is valid: " "${result}"

    printf ${result}
}

printf "\n %s %s \n" "name1: " "$name1"
printf "\n %s %s \n" "name2: " "$name2"
printf "\n %s %s \n" "name3: " "$name3"


r1=0
r2=0
r3=0

r1=$(is_valid_name $name1)
r2=$(is_valid_name $name2)
r3=$(is_valid_name $name3)

printf "\n  0 ->  Not valid var name\n"
printf "\n  1 ->  Valid var name \n"

printf "\n  %s %s \n" "is valid name1 : " "${r1}"
printf "\n  %s %s \n" "is valid name2 : " "${r2}"
printf "\n  %s %s \n" "is valid name3 : " "${r3}"