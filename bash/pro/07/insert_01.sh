#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : insert a string s in container string in position pos.   │
#│               Function return a string.                                │
#└────────────────────────────────────────────────────────────────────────┘

clear

insert()
{
    local container=$1
    local s=$2             # string to insert  
    local pos=$3
    local result=;

    local left=${container:0:$(( $pos ))}
    local right=${container:$(( $pos ))}
    local result=${left}${s}${right}

    #printf "\n *** insert() ... begin \n"
    #printf "\n %s %s \n" "container : " "${container}"
    #printf "\n %s %s \n" "s         : " "${s}"
    #printf "\n %s %s \n" "pos       : " "${pos}"
    #printf "\n %s %s \n" "left : " "${left}"
    #printf "\n %s %s \n" "right: " "${right}"
    #printf "\n %s %s \n" "result: " "${result}"
    #printf "\n *** insert() ... end \n"

    printf "${result}\n"
}

printf "\n Insert a string s into a container string. Example 01. \n"


container="The old have a farm."
s="-McDonald-"
pos=7

printf "\n %s %s \n" "container : " "${container}"
printf "\n %s %s \n" "s         : " "${s}"
printf "\n %s %s \n" "pos       : " "${pos}"

result=`insert "${container}" ${s} ${pos} `

printf "\n %s %s \n\n" "result: " "${result}"