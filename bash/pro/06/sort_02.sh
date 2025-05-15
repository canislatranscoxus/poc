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
  if (( $1 > $2 ))
  then
    if (( $2 > $3 ))
    then
      let _max=$1
      let _median=$2
      let _min=$3  
    
    elif (( $1 > $3 ))
    then
      let _max=$1
      let _median=$3
      let _min=$2  
    else
      let _max=$3
      let _median=$1
      let _min=$2  
    fi

  elif (( $2 > $3 ))
  then

    if (( $3 > $1 ))
    then
      let _max=$2
      let _median=$3
      let _min=$1  
    else
      let _max=$2
      let _median=$1
      let _min=$3  
    fi

  else
      let _max=$3
      let _median=$2
      let _min=$1  
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