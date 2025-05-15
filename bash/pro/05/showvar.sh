#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description: list 5.1. showvar                                         │
#│                                                                        │
#│ usage: in the terminal you can set the value of x and next run this    │
#│        script.                                                         │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

clear



if [[ ${x+X} = X ]] ## If $x is set              
then              
  if [[ -n $x ]] ## if $x is not empty              
  then              
    printf "  \$x = %s\n" "$x"              
  else              
    printf "  \$x is set but empty\n"              
  fi              
else              
  printf " %s is not set\n" "\$x"              
fi            