#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Exercise 2_2 : write a bash script that generate random float numbers  │
#│                similar to the these                                    │
#│                                                                        │
#│                3415.2694                                               │
#│                3226.3027                                               │
#│                1085.2894                                               │
#│                                                                        │
#│                and send the output to a file called 2_2.tmp            │
#│                and to the output stream                                │
#│                in the console                                          │
#└────────────────────────────────────────────────────────────────────────┘

clear

rm 2_2.tmp

# this can generate number with more than 4 digits in the integer or decimal part. 
printf "%4s"."%4.04d \n"  $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM | tee 2_2.tmp 
