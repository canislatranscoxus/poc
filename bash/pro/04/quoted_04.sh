#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: example using quotes                                      │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "\n this is an example of concatenating string constant and variable"

animal=cat
t1="I like my ${animal}"
t2='${animal} is super agile'


printf "\n animal: \n" 
printf ${animal}

printf "\n t1   : \n"
echo ${t1}
printf "%s" "${t1}"

printf "\n t2   : \n"
echo ${t2}
printf "%s" "${t2}"


printf "\n \n"