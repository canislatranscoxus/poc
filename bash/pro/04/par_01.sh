#!/bin/bash

#┌───────────────────────────────────────────────────────────────────────────┐
#│ Description: example using parsing options                                │
#│                                                                           │
#│ options with arguments                                                    │
#│   -a     < animal >                                                       │
#│   -b     < book   >                                                       │
#│   -c     < color  >                                                       │
#│                                                                           │
#│ options with out arguments:                                               │
#│   -s     save automatically                                               │
#│   -t     translate to Swedish, French and Spanish                         │
#│   -v     Verbose                                                          │
#│                                                                           │
#│ usage example:                                                            │ 
#│  . par_01.sh -a dog -b "The hound of the Baskervilles" -c yellow -s -t -v 
#└───────────────────────────────────────────────────────────────────────────┘

clear

printf "help \n"
printf "run the script using the following options \n"
printf " options with arguments \n"
printf "   -a     < animal > \n"
printf "   -b     < book   > \n"
printf "   -c     < color  > \n"
printf "                     \n"
printf " options with out arguments: \n"
printf "   -s     save automatically \n"
printf "   -t     translate to Swedish, French and Spanish \n"
printf "   -v     Verbose \n"


#get script name without path
progname=${0##*/}

#default values
animal=cat
book=aladdin
color=red
save=0
translate=0
verbose=0

# accepted options 
optstring=a:b:c:stv

## The loop calls getopts until there are no more options on the command line              
## Each option is stored in $opt, any option arguments are stored in OPTARG              

while getopts $optstring opt
do
    case $opt in
        a) animal=$OPTARG ;;
        b) book=$OPTARG ;;
        c) color=$OPTARG ;;
        s) save=1 ;;
        t) translate=1 ;;
        v) verbose=1 ;;
        *) exit 1 ;;
    esac
done

printf "this are the options you entered"
printf "%s %s \n" "progname :" $progname
printf "%s %s \n" "animal   :" $animal
printf "%s %s \n" "book     :" $book
printf "%s %s \n" "color    :" $color

printf "%s %s \n" "save     :" $save
printf "%s %s \n" "translate:" $translate
printf "%s %s \n" "verbose  :" $verbose

printf "%s %s \n" "num of args: " $#
printf "* of args: \n" 
printf "%s " $*
printf "\n @ of args: %s \n"
printf "%s " $@

printf "\n\n"