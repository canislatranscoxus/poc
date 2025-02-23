#┌────────────────────────────────────────────────────────────────────────┐
#│                                                                        │
#│ Description: Example of array variables                                │
#│                                                                        │
#│ usage:                                                                 │
#│     ./arr_01.sh                                                        │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

colors[0]="red"
colors[1]="blue"
colors[2]="yellow"

echo "colors[0] is: " ${colors[0]}
echo "colors[1] is: " ${colors[1]}
echo "colors[2] is: " ${colors[2]}

echo "print all the elements of array colors"
echo "colors[@] is: " ${colors[@]}


echo "Number of elements in the array: " ${#colors[@]}

echo "element 2: " ${colors[2]}
echo "Number of characters of element 2: " ${#colors[2]}

echo "replace element blue by green"
echo ${colors[@]/blue/green }
echo "colors[@] is: " ${colors[@]}
