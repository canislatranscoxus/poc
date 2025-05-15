#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : example of function 01                                   │
#│               input is a number, output double of the number           │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Example, call a function to calculate the double of a number \n"

pertwo() 
{        
  n=${1}      
  #printf "%s %s \n" "local n: " $n

  let result=$(($n*2))
  #printf "%s %s \n" "local result: " $result
  return $result
}       

unset n
unset result

n=5
printf "%s %s \n" "my number: " ${n}


#result=pertwo ${n} 
pertwo "5"
result=$?

printf "%s %s \n" "the double of my number is: " ${result}

