'''
description: in this example we get all the charges from open pay.

'''

import json
from Charges import Charges

charges = Charges()

response = charges.get_all()
a = response.json()

print( '\ncharge_id \t order_id \t status\n' )

for row in a:
    print( '{} \t\t {} \t {}'.format( row[ 'id' ], row[ 'order_id' ], row[ 'status' ] ) )

print( '\n...end' )    