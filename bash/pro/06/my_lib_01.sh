#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Description : Sample library.                                          │
#│                                                                        │
#│ Usage: in linux terminal type the next command to load the library     │
#│                                                                        │
#│       . my_lib_01.sh                                                   │
#│                                                                        │
#│       now we can use the functions                                     │
#└────────────────────────────────────────────────────────────────────────┘

clear

##              
## Set defaults              
##              
prompt=" ==> "              
template='<!DOCTYPE html>              
<html lang="en">              
  <head>              
    <meta charset=utf-8>              
    <title>%s</title>              
    <link href="%s" rel="stylesheet">              
  </head>              
  <body>              
    <h1>%s</h1>              
    <div id=main>              
    </div>              
  </body>              
</html>              
'              
##              
## Define shell functions              
##              
die() #@ DESCRIPTION: Print error message and exit with ERRNO code              
{     #@ USAGE: die ERRNO MESSAGE ...              
  error=$1              
  shift              
  [ -n "$*" ] && printf "%s\n" "$*" >&2              
  exit "$error"              
}              
usage() #@ Print script's usage information              
{       #@ USAGE: usage              
  printf "USAGE: %s HTMLFILE\n" "$progname"              
}              
version() #@ Print scrpt's version information              
{          #@ USAGE: version              
  printf "%s version %s" "$progname" "${version:-1}"              
}              
#@ USAGE: readline var prompt default              
#@ DESCRIPTION: Prompt user for string and offer default              
##              
#@ Define correct version for your version of bash or other shell              
bashversion=${BASH_VERSION%%.*}              
if [ ${bashversion:-0} -ge 4 ]              
then              
  ## bash4.x has an -i option for editing a supplied value              
  readline()              
  {              
    read -ep "${2:-"$prompt"}" -i "$3" "$1"              
  }              
elif [ ${bashversion:-0} -ge 2 ]              
then              
  readline()              
  {              
    history -s "$3"              
    printf "Press up arrow to edit default value: '%s'\n" "${3:-none}"              
    read -ep "${2:-"$prompt"}" "$1"              
  }              
else              
  readline()              
  {              
    printf "Press enter for default of '%s'\n" "$3"              
    printf "%s " "${2:-"$prompt"}"              
    read              
    eval "$1=\${REPLY:-"$3"}"              
  }              
fi              
if [ $# -ne 1 ]              
then              
  usage              
  exit 1              
fi              
filename=$1              
readline title "Page title: "              
readline h1 "Main headline: " "$title"              
readline css "Style sheet file: " "${filename%.*}.css"              
printf "$template" "$title" "$css" "$h1" > "$filename"            

