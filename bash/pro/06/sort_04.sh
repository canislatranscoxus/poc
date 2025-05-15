#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : example of function                                      │
#│               input 3 numbers                                          │
#│               return as output sorted list                             │
#│               the 3 from smallest to biggest                           │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

#@ USAGE example: _max3 9 3 6
# output: 
#   min   : 3
#   median: 6
#   max   : 9 

_max3() 
{
  # in this function, we will sort the parameter list, from smallest to biggest

  # check if we have 3 parameters
  (( $# < 3 )) && return 4


  # if param_1 > param_2 then swap positions
  (( $1 > $2 )) && set "$2" "$1" "$3"

  # if param_2 > param_3 then swap positions
  (( $2 > $3 )) && set "$1" "$3" "$2"

  # if param_1 > param_2 then swap positions
  (( $1 > $2 )) && set "$2" "$1" "$3"

  let _min=$1  
  let _median=$2
  let _max=$3

  printf "%s %s \n" "_min= " $_min
  printf "%s %s \n" "_median= " $_median
  printf "%s %s \n" "_max= " $_max

  

}       

clear
printf "\n Example, sort 3 numbers \n "
printf "\n enter 3 numbers :"
read nums

a=($nums)

printf "my array: \n"
printf "%s \n" "${a[@]}"

_max3 "${a[@]}"