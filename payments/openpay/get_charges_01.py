'''
description:

In this example we use the openpay REST API
to get the charges that belong to a purchase order,
to validate the status. 

We do not store card data, we just get the transaction data from openpay website.

output:



links:
    https://www.openpay.mx/docs/op-form-charge.html
    https://www.openpay.mx/api/?shell#con-redireccionamiento
    https://www.openpay.mx/docs/testing.html

'''

import json
import requests
import os


# prepare parameters
OPENPAY_URL         = os.environ[ 'OPENPAY_URL'         ]
OPENPAY_MERCHANT_ID = os.environ[ 'OPENPAY_MERCHANT_ID' ]
OPENPAY_PRIVATE_KEY = os.environ[ 'OPENPAY_PRIVATE_KEY' ]

url = '{}{}/charges'.format( OPENPAY_URL, OPENPAY_MERCHANT_ID)
params = {
   'order_id'       : 'oid-002',
}

headers = {'Content-type': 'application/json' }

# request charge
r = requests.get( url
    , params    = params
    , headers   = headers
    , auth      = ( OPENPAY_PRIVATE_KEY, None ) )

# print response
print( 'status code: {}'.format( r.status_code ) ) 
print( json.dumps( r.json(), indent= 3 ) )

print( '\n' )
print( 'order_id: {}'.format( r.json()[0][ 'order_id' ] ) )
print( 'status  : {}'.format( r.json()[0][ 'status' ] ) )

print(  '... end.' )
