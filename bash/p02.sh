#!/bin/bash

let file_size = 0
let total_size = 0

clear
echo 'print the name of my eagle images \n'

for i in /home/art/Pictures/eagle/*.jpg
do
   echo $i
   let file_size=`ls -l $i | tr -s " " | cut -f5 -d " " `
   let total_size=$total_size+$file_size

done

echo "total size: " $total_size " bytes" | tee eagle_img_results.txt
