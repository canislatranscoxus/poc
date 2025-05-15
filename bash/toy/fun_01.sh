#┌────────────────────────────────────────────────────────────────────────┐
#│                                                                        │
#│ Description: Example of functions                                      │
#│                                                                        │
#│ usage:                                                                 │
#│     ./arr_01.sh                                                        │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

function greetings()
{
    echo "hello world, function: greeting"
}

function i_like( )
{
    num=$1 
    fruit=$2
    echo "I like " $num " " $fruit
}

greetings
i_like 10 bananas
