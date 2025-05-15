#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: replace all the substrings that matches the pattern       │
#│              var//pattern/string                                       │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Replace, example 1. \n "

animal=elephant
printf "%s %s \n" "animal: " $animal
printf "%s %s \n" "hidden animal: " "${animal//?/*}"

printf "%s %s \n" "hidden animal: " "${animal//e/*}"

animal=flying.fish
printf "%s %s \n" "animal: " $animal
printf "%s %s \n" "hidden animal: " "${animal//f/F}"
