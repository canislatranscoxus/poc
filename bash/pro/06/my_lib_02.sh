#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Sample library.                                          │
#│                                                                        │
#│ Usage: in linux terminal type the next command to load the library     │
#│                                                                        │
#│       . my_lib_02.sh                                                   │
#│                                                                        │
#│       now we can use the functions                                     │
#└────────────────────────────────────────────────────────────────────────┘

clear

##              
## Set defaults              
##              
prompt=" ==> "              

##              
## Define shell functions              
##              
say_hello() #@ DESCRIPTION: Print error message and exit with ERRNO code              
{     #@ USAGE: say_hellow              
                
  printf "\n hello my friends  \n" 

}              

usage()
{
  printf "USAGE: %s HTMLFILE\n" "$progname"              
}

version() 
{          #@ USAGE: version              
  printf "%s version %s" "$progname" "${version:-1}"              

  bashversion=${BASH_VERSION%%.*}
  printf "%s %s \n" "version: " ${bashversion}

}              
