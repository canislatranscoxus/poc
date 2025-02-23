#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: While loop example 02                                     │
#│              break Loop,                                               │
#│                                                                        │
#│ usage:                                                                 │
#│     ./while_02.sh                                                      │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

function show_menu()
{
    clear
    echo "1) show IP info"
    echo "2) who command"
    echo "3) exit"

}

selection=0

#while [ $selection -ne 3 ]
while true
do
    read -p "Enter worked hours followed by hourly wage (-1 to quit): " hours wage

    if [ $hours -eq -1 ]
    then
        break
    fi

    pay=$(( hours * wage ))
    echo "pay: " $pay " US dollars"
done

