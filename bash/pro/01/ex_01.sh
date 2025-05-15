#!/bin/bash

#┌────────────────────────────────────────────────────────────────────────┐
#│ Excercise 1:                                                           │
#│                                                                        │
#│ Write a script that creates a directory called tmp_bash_01 inside      │
#│ $HOME. Populate this directory with two subdirectories:                │
#│ bin and scripts. You must create the following tree structure          │
#│                                                                        │
#│  home/                                                                 │
#│    |                                                                   │
#│    +--- tmp_bash_01                                                    │
#│           |                                                            │
#│           +--- bin                                                     │
#│                scripts                                                 │
#│                                                                        │
#│ usage:                                                                 │
#│     ./ex_01.sh                                                         │
#└────────────────────────────────────────────────────────────────────────┘
# 

cd 
mkdir tmp_bash_01
cd tmp_bash_01
mkdir bin
mkdir scripts