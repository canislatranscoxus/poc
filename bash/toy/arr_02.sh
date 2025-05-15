#┌────────────────────────────────────────────────────────────────────────┐
#│                                                                        │
#│ Description: Read fruits.txt and populate an array                     │
#│                                                                        │
#│ usage:                                                                 │
#│     ./arr_01.sh                                                        │
#└────────────────────────────────────────────────────────────────────────┘
# 

#!/bin/bash

clear

rows=`cat fruits.txt`

echo "the rows array elements are:"
echo ${rows[@]}

echo ""
echo "the fruits in rows array are:"
for i in $rows
do
    echo $i
done

echo ""