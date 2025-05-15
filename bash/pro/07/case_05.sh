#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Convert a word to upper case using a big  switch case...        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear


printf "\n Convert to upper case. Example 05, using a BIG switch case. \n"

# Convert to Uppercase the first char of the string              
capitalize()              
{
    case $1 in              
        a*) _UPR=A ;; b*) _UPR=B ;; c*) _UPR=C ;; d*) _UPR=D ;;              
        e*) _UPR=E ;; f*) _UPR=F ;; g*) _UPR=G ;; h*) _UPR=H ;;              
        i*) _UPR=I ;; j*) _UPR=J ;; k*) _UPR=K ;; l*) _UPR=L ;;              
        m*) _UPR=M ;; n*) _UPR=N ;; o*) _UPR=O ;; p*) _UPR=P ;;               
        q*) _UPR=Q ;; r*) _UPR=R ;; s*) _UPR=S ;; t*) _UPR=T ;;              
        u*) _UPR=U ;; v*) _UPR=V ;; w*) _UPR=W ;; x*) _UPR=X ;;              
        y*) _UPR=Y ;; z*) _UPR=Z ;; *) _UPR=${1%${1#?}} ;;              
    esac     
    
    result="$_UPR""${1#?}"
    printf "%s\n" "${result}"
     
}

# Convert to uppercase a string
to_upper()
{
    word=$1
    first=;
    result=;

    while [ -n "$word" ]
    do 
        word=`capitalize ${word}`
        first=${word:0:1}
        result="${result}""$first"

        # remove the first char
        word=${word#?}

    done
    printf "%s\n" "${result}"
}

s1="turtles"
printf "\n %s %s \n" "s1  : "  "${s1}"

s2=`capitalize ${s1}` 
printf "\n  %s %s \n" "Capitalized: " "${s2}"

s3=`to_upper ${s1}`
printf "\n  %s %s \n" "Uppercase: " "${s3}"
