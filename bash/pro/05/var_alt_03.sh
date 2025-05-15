#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: play with var alternate +                                 │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n var alternate \n"

printf "\n Example 1. \n"
var=              
for n in a b c d e f g              
do              
    var="${var:+$var}$n"              
done            
printf "%s" ${var}



printf "\n \n"
echo $var