import json

pet = { 
    'name'   : 'Patitas',
    'specie' : 'cat',
    'age'    : 1
 }

msg = 'id = {}. {name} is a {specie} of {age} years.'.format( 712, **pet )


print( '\n', msg, '\n' )