#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: Indirect reference                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Indirect Reference \n "

fruit=papaya
food=fruit

printf "%s %s \n" "fruit: " $fruit
printf "%s %s \n" "food: " $food

printf "%s %s \n" "our favourite food is : " ${!food}

printf "expanded food is : " 
eval "\$$food"