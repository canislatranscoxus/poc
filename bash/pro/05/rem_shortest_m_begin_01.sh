#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: remove shortest match from the begin of the string        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "remove shortest match from the end of the string\n "

s=Wollogong


printf "%s %s \n" "s: " $s 
s=${s#*o}
printf "%s %s \n" "s: " $s 
s=${s#*o}
printf "%s %s \n" "s: " $s 
s=${s#*o}
printf "%s %s \n" "s: " $s 


s=Mississipi
patter=i*
printf "%s %s \n" "s: " $s 
s=${s#*i}
printf "%s %s \n" "s: " $s 
s=${s#*i}
printf "%s %s \n" "s: " $s 
s=${s#*i}
printf "%s %s \n" "s: " $s 
s=${s#*i}
printf "%s %s \n" "s: " $s 
