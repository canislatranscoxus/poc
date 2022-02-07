import json

pet = { 
    'name'   : 'Patitas',
    'specie' : 'cat',
    'age'    : 1
 }

for k, v in pet.items():
    print( '{}: {}'.format( k, v ) )


print( '\n complex dictionary \n'  )



from datetime import date
d1 = date( 2001, 11, 1 )
d2 = date( 2002, 12, 2 )

my_dates = {
    'd1' : d1,
    'd2' : d2
}

for k,v in my_dates.items():
    print( '{}: {}'.format( k, v.isoformat()  ) )

print( '\n end. \n' )