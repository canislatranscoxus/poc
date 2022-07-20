'''

description: get geolocation from zipcode

https://pypi.org/project/pgeocode/

'''

import pgeocode

nomi   = pgeocode.Nominatim( 'mx' )
result = nomi.query_postal_code( "66634" )

print( '\n\n' ) 
print( result )

print( '\n lat: {}'.format( result.latitude ) )
print( 'lon: {} \n\n '.format( result.longitude ) )

