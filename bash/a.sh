#------------------------------------------------------------------------------
# usage:
#       ./a.sh cat climbs
#
#------------------------------------------------------------------------------

#!/bin/bash

echo "01 - , test 01"

p1=$1
p2=$2
face=$3

echo "\n\n parameters"
echo "p1: $p1"
echo "p2: ${p2}"
echo "face: ${face} "

echo $'\n args:'
echo $p1
echo ${p2}
echo ${face}

case $p1 in
cat)
  echo "we have a CAT"
  ;;

dog)
  echo "dog bites"
  ;;

*)
  echo "we like all animals"
  ;;
esac

