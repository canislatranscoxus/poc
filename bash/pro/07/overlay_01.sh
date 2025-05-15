#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : overlay, overwrite a string container with string s,     │
#│               starting from position pos.                              │
#│               Function return a string.                                │
#└────────────────────────────────────────────────────────────────────────┘

clear

overlay()
{
    local container=$1
    local s=$2             # string to insert  
    local pos=$3
    local result=;

    local left=${container:0:$(( $pos ))}
    local right=${container:$(( $pos + ${#s} ))}
    local result=${left}${s}${right}

    printf "\n *** overlay() ... begin \n"
    printf "\n %s %s \n" "container : " "${container}"
    printf "\n %s %s \n" "s         : " "${s}"
    printf "\n %s %s \n" "pos       : " "${pos}"
    printf "\n %s %s \n" "left : " "${left}"
    printf "\n %s %s \n" "right: " "${right}"
    printf "\n %s %s \n" "result: " "${result}"
    printf "\n *** overlay() ... end \n"

    printf "${result}\n"
}

printf "\n overlay, overwrite a string container with string s. Example 01. \n"


container="She got a hound that reminds me..."
s="SMILE"
pos=10

printf "\n %s %s \n" "container : " "${container}"
printf "\n %s %s \n" "s         : " "${s}"
printf "\n %s %s \n" "pos       : " "${pos}"

result=`overlay "${container}" ${s} ${pos} `

printf "\n %s %s \n\n" "result: " "${result}"