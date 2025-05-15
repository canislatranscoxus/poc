#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Exercise 2_2 : write a bash script that generate random float numbers  │
#│                similar to the these                                    │
#│                                                                        │
#│                3415.2694                                               │
#│                3226.3027                                               │
#│                1085.2894                                               │
#│                                                                        │
#│                and send the output to a file called 2_3.tmp            │
#│                and to the output stream                                │
#│                in the console                                          │
#└────────────────────────────────────────────────────────────────────────┘

# this can generate number with more than 4 digits in the integer or decimal part. 
#printf "%04d"."%04d \n"  $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM | tee 2_2.tmp 


clear
rm 2_3.tmp

n=0
n_int=0
n_dec=0
lines=""

for ((i=0;i<=3;i++))
do
    n=0

    printf "%s %d \n" "i: " $i

    # generate the integer and decimal part with zero left padded
    printf -v n_int "%04d" $RANDOM
    printf -v n_dec "%04d" $RANDOM
    
    # crop the number to fit in the width
    printf -v n_int "%4.4s" $n_int
    printf -v n_dec "%4.4s" $n_dec

    # make the complete number
    printf -v n "%s"."%s" $n_int $n_dec
    printf "%s \n" $n

    #printf -v lines "%s\r\n%s" $lines $n
    lines=$lines"\\r\\n"$n



    printf "lines: \n "
    printf "%s \n\n" $lines


    #printf "%s \n" n1 n2 n3 | tee 2_2.tmp 
done


# print number to output stream and to a file
printf "%b"  $lines | tee 2_3.tmp 