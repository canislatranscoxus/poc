#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: example using quotes                                      │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

s1=\ this"is a"'demonstration of'\ quotes\ and\ escapes
printf "%s %s \n" "example 1: " $s1

s1=cat\ dog\ fish\ turtle\ bunny
printf "%s %s \n" "example 2: " $s1

s1="apple \ banana \ orange  \n lemon \n pineapple \n melon \n strawberry \n blue_berry \n"
printf "%s %s \n" "example 3: " $s1

s1='apple \ banana \ orange  \n lemon \n pineapple \n melon \n strawberry \n blue_berry \n'
printf "%s %s \n" "example 4: " $s1
