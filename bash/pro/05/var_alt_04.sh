#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: play with var alternate +                                 │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n var alternate \n"

printf "\n Example 4. \n"

var=              
n="bananas_and_strawberries"



if [ -n "$var" ]              
then              
    var="$var $n"              
else              
    var=$n              
fi    

printf "\n \n"
printf "%s" $var

printf "\n \n"



printf "\n Example 5. \n"
var=              
n="ninjas_turtles"
              
[ -n "$var" ] && var="$var $n" || var=$n


printf "\n \n"
printf "%s" $var

printf "\n \n"
