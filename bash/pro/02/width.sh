#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: print formating - width specification                     │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘
# 

clear

printf "\n padding zeros - integers \n"
printf "%04d \n" 10 20 30

printf "\n string and floats \n"
printf "%5.3s %6.4f \n" "Anastasia" 132 "Elsa" 20.141592 "Olaf" 30.56
