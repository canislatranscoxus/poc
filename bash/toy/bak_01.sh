#┌────────────────────────────────────────────────────────────────────────┐
#│                                                                        │
#│ Description: Make a backup                                             │
#│                                                                        │
#│ usage:                                                                 │
#│     ./arr_01.sh                                                        │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

day=`date +"%d"`
month=`date +"%m"`
year=`date +"%Y"`

function backup()
{
    echo "date: " $year "-" $month "-" $day
    echo "creating backup ..."
    tar -czvf fruits-$year-$month-$day.tar.gz fruits.txt 2>/dev/null >> backup.log 
    echo "backup end."
}

backup

