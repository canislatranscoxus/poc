#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: replace the first substring that matches the pattern      │
#│              var/pattern/string                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear

printf "Replace, example 2. \n "

animal=beatle


printf "%s %s \n" "animal: " $animal
printf "%s %s \n" "hidden animal ?: " "${animal/?/*}"

printf "%s %s \n" "hidden animal e: " "${animal/e/*}"

animal=giagant.yellow.hornet
printf "%s %s \n" "animal: " $animal
printf "%s %s \n" "hidden animal . : " "${animal/[[:punct:]]/*}"
