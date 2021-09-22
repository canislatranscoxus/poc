'''
description: in this example we get all the charges from open pay.

'''

import json
from Charges import Charges

charges = Charges()

row = charges.get_charge( 16 )


print( '\ncharge_id \t\t order_id \t status\n' )

print( '{} \t\t {} \t {}'.format( row[ 'id' ], row[ 'order_id' ], row[ 'status' ] ) )

print( '\n...end' )    