#!/bin/bash

#┌───────────────────────────────────────────────────────────────────────────┐
#│ Excercise: 4.2                                                            │
#│                                                                           │
#│ Find the error in the snippet                                             │
#│                                                                           │
#│                                                                           │
#│                                                                           │
#│                                                                           │
#└───────────────────────────────────────────────────────────────────────────┘

clear

printf "help \n"

year=$( date +%Y )                    
month=$( date +%m )                    
day=$( date +%d )                    
hour=$( date +%H )                    
minute=$( date +%M )                    
second=$( date +%S )   

printf "%s %s \n" "year   : " $year
printf "%s %s \n" "month  : " $month
printf "%s %s \n" "day    : " $day

printf "%s %s \n" "hour   : " $hour
printf "%s %s \n" "minute : " $minute
printf "%s %s \n" "second : " $second