#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Process char by char.                                    │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Process char by char. Example 01 \n"

s1="Welcome to the junglE"; 
allbutfirst=${s1#?}
allbutlast=${s1%?}

xxxfirst=${s1#???}
xxxlast=${s1%???}

first=${s1%"$allbutfirst"}
last=${s1#"$allbutlast"}

printf "%s %s \n" "s1         : " "${s1}"
printf "%s %s \n" "allbutfirst: " "${allbutfirst}"
printf "%s %s \n" "allbutlast : " "${allbutlast}"

printf "%s %s \n" "xxxfirst   : " "${xxxfirst}"
printf "%s %s \n" "xxxlast    : " "${xxxlast}"

printf "%s %s \n" "first      : " "${first}"
printf "%s %s \n" "last       : " "${last}"
