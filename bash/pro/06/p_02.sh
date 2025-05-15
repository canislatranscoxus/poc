#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : this script include library my_lib_02.sh                 │
#│               and call its functions                                   │
#│                                                                        │
#│                                                                        │
#└────────────────────────────────────────────────────────────────────────┘

# include my_lib_02.sh
. my_lib_02.sh


clear


# call functions

printf "\n calling function say_hello \n"
say_hello

printf "\n calling function version \n"
version

printf "\n end. \n"