#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : trim unwanted char at beginning and end of a string.     │
#│               Function return a string.                                │
#└────────────────────────────────────────────────────────────────────────┘

clear

trim()
{
    local s=$1            # string
    local unwanted_ch=$2  # unwanted char   
    local result=$s;

    local begin_pattern=${unwanted_ch}"*"
    local end_pattern="*"${unwanted_ch}

    #printf "\n *** trim() ... begin \n"
    #printf "\n %s %s \n" "s         : " "${s}"
    #printf "\n %s %s \n" "unwanted_ch       : " "${unwanted_ch}"
    #printf "\n %s %s \n" "begin_pattern : " "${begin_pattern}"
    #printf "\n %s %s \n" "end_pattern: " "${end_pattern}"

    local i=0

    while true ;
    do
        case $result in
        ${begin_pattern}) result=${result#?} ;; # remove first char
        ${end_pattern}) result=${result%?}   ;; # remove last  char
        *) break ;; # no more leading or trailing unwanted char
        esac
    done


    #printf "\n %s %s \n" "result: " "${result}"
    #printf "\n *** trim() ... end \n"

    printf "${result}\n"
}

printf "\n trim unwanted char at beginning and end of a string. \n"

printf "\n Example 01. remove ~ \n" 
s="~~sleeping beauty~~~"
unwanted_ch="~"
result=`trim "${s}" "${unwanted_ch}" `
printf "\n %s %s \n\n" "result: " "${result}"

printf "\n Example 02. remove zeros 0 \n" 
s="00000003.141592000000"
unwanted_ch="0"
result=`trim "${s}" "${unwanted_ch}" `
printf "\n %s %s \n\n" "result: " "${result}"

