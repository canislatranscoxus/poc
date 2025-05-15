#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: default = is similar to default -                         │
#│              But also, default = asign the value to the variable       │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n default flavor is vanilla \n"


printf "\n example 0. (var is unset) empty or unset var \n"
unset flavor
echo "ice_cream" ${flavor:=vanilla}"***"


printf "\n example 1. (var is empty) empty or unset var \n"
flavor=
echo "ice_cream" ${flavor:=vanilla}"***"

printf "\n example 2.  var=strawberry \n"
flavor=strawberry
echo "ice_cream" ${flavor:=vanilla}"***"

printf "\n example 3. (var is unset) if var is unset give me default ? \n"
unset flavor
echo "ice_cream" ${flavor=vanilla}"***"

printf "\n example 4. (var is empty) if var is unset give me default ? \n"
flavor=
echo "ice_cream" ${flavor=vanilla}"***"
