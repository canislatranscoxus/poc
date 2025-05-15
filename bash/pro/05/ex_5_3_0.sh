#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Exercise 5.3 :                                                         │
#│               Given var=192.168.0.123,                                 │
#│               write a script that uses parameter expansion             │
#│               to extract the second number, 168.                       │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "extract the second number from IP 192.168.0.123 \n "
printf "\n "

unset var
unset a

var=192.168.0.123

# replace dot by spaces
my_nums=${var//./ }

# convert to array
a=(${my_nums})

printf "%s \n " "array: " "${a[@]}"

printf "%s %s \n" "second number is: " "${a[1]}"