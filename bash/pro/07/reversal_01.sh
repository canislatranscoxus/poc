#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Process char by char.                                    │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Process char by char. Example 03, reversal. \n"

s1="Welcome to the junglE"; 
allbutfirst=${s1#?}
allbutlast=${s1%?}

first=${s1%"$allbutfirst"}
last=${s1#"$allbutlast"}

printf "%s %s \n" "s1         : " "${s1}"
printf "%s %s \n" "allbutfirst: " "${allbutfirst}"
printf "%s %s \n" "allbutlast : " "${allbutlast}"

printf "\n looping in reversal one by one character \n\n" 

var=${s1}
ch=;

while [ -n "$var" ]
do
    allbutlast=${var%?}
    ch=${var#"$allbutlast"}

    printf "%s " "${ch}"
    var=${allbutlast}
done

printf "\n\n end. \n"
