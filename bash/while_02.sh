#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: While loop example 02                                     │
#│              Loop,                                                     │
#│              display menu, do something until                          │
#│              user want to exit                                         │
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
    show_menu
    read selection

    case $selection in
        1)ifconfig;;
        2)who;;
        3)clear;exit;;
    esac

    echo "press Enter to continue ..."
    read junk

done

