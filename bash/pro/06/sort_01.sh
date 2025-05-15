#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : example of function                                      │
#│               input 3 numbers                                          │
#│               return as output sorted the 3 from smallest to biggest   │
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
  a=$1
  b=$2
  c=$3

  if (( $a > $b ))
  then
    if (( $b > $c ))
    then
      let _max=$a
      let _median=$b
      let _min=$c  
    
    elif (( $a > $c ))
    then
      let _max=$a
      let _median=$c
      let _min=$b  
    else
      let _max=$c
      let _median=$a
      let _min=$b  
    fi

  elif (( $b > $c ))
  then

    if (( $c > $a ))
    then
      let _max=$b
      let _median=$c
      let _min=$a  
    else
      let _max=$b
      let _median=$a
      let _min=$c  
    fi

  else
      let _max=$c
      let _median=$b
      let _min=$a  
  fi 

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