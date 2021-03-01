from __future__ import print_function

import json

j = { 
    'animal' : 'cat' ,
    'pet' : {}
}

j[ 'pet' ][ 'name'  ] = 'little paws'
j[ 'pet' ][ 'color' ] = 'brindle'

print( json.dumps( j, indent= 4 ) )