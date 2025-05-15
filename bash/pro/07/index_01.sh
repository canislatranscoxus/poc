#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : return the position of subtring in a string.             │
#│               Function return a string.                                │
#└────────────────────────────────────────────────────────────────────────┘

clear

# return the position of subtring in a string
_index()
{
    local s=$1
    local substring=$2 
    local idx=-2;
    local tmp=;

    case $s in
    "") idx=-1 ;;
    
    *"$substring"*) 
        ## extract up to beginning of the matching portion  
        tmp=${s%%"$substring"*}
        
        #get index position
        idx=${#tmp}
        ;;

    *) idx=-1 ;;
    esac

    printf "${idx}\n"
}

printf "\n return the position of subtring in a string. Example 01. \n"

s="Lay a_wisper on my pillow."
substring="Xwisper"
pos=;

printf "\n %s %s \n" "s         : " "${s}"
printf "\n %s %s \n" "substring : " "${substring}"

pos=`_index "${s}" "${substring}"`
printf "\n %s %s \n" "pos       : " "${pos}"

