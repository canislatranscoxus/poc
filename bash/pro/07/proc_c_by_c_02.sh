#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Process char by char.                                    │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Process char by char. Example 02 \n"

s1="Welcome to the junglE"; 
allbutfirst=${s1#?}
allbutlast=${s1%?}

first=${s1%"$allbutfirst"}
last=${s1#"$allbutlast"}

printf "%s %s \n" "s1         : " "${s1}"
printf "%s %s \n" "allbutfirst: " "${allbutfirst}"
printf "%s %s \n" "allbutlast : " "${allbutlast}"

printf "\n looping one by one character \n\n" 

var=${s1}
ch=;

while [ -n "$var" ]
do
    allbutfirst=${var#?}
    ch=${var%"$allbutfirst"}

    printf "%s " "${ch}"
    var=${allbutfirst}
done

printf "\n\n end. \n"
