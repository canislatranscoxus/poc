#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Convert month name to number using index.                │
#│               Function return a number.                                │
#└────────────────────────────────────────────────────────────────────────┘

clear

# return the position pos of subtring in a string s
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

    echo "${idx}"
}



_month2num()
{
    local month=$1
    local num=0 
    local months="JAN.FEB.MAR.APR.MAY.JUN.JUL.AUG.SEP.OCT.NOV.DEC."

    # convert to upper case
    month=`echo $month | tr [a-z] [A-Z]`

    # get first 3 letters of month
    month=${month:0:3}

    # get the index of the month in the months string
    idx=`_index "${months}" "${month}" `
    
    # calculate the number of the month
    if (( idx >= 0 )) 
    then
        num=$(( idx / 4 + 1 ))
    fi
    
    #printf "\n %s %s \n" "idx: " "${idx}"
    #printf "\n %s %s \n" "num: " "${num}"

    printf "${num}\n"
}

printf "\n return the position of subtring in a string. \n"


month="februarY"
num=;
num=`_month2num "${month}"`
printf "\n Example 01. \n"
printf "\n %s %s \n" "month: " "${month}"
printf "\n %s %s \n" "month num  : " "${num}"


month="Xdecember"
num=;
num=`_month2num "${month}"`
printf "\n Example 02. \n"
printf "\n %s %s \n" "month: " "${month}"
printf "\n %s %s \n" "month num  : " "${num}"



printf "\n End. \n"
