#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: default = is similar to default -                         │
#│              But also, default = asign the value to the variable       │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n example default 02. Assign default zero to variable n \n"

unset n              
while :              
do              
    echo :$n:              
    [ ${n:=0} -gt 3 ] && break ## set $n to 0 if unset or empty              
    n=$(( $n + 1 ))              
done              