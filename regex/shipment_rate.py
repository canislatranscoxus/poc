'''
Description: in this example we extract the numbers from strings.
             The idea is to know the shipment rate.
'''

import re

pattern = '\$?((\d{1,3}(\,){0,1})*\d{1,3}(\.\d{1,2}){0,1})\s'
prog = re.compile( pattern )


a = [
'$149.13 MXN - FEDEX Fedex Express Saver',
'$205.07 MXN - FEDEX Standard Overnight',
'$180.0 MXN - DHL DHL Terrestre',
'$204 MXN - DHL DHL Express',
'$119.69 MXN - CARSSA Nacional',
]

print( '\The rates are:' )

for my_string in a:
    #result = re.match( pattern, my_string )
    result = prog.match( my_string )
    #print( result )
    if result != None:
        rate = result.group( 1 )
        print( 'Entire match: {},\trate: ***{}***'.format( result.group( 0 ), result.group( 1 ) )  )

print( '\n End.' )        