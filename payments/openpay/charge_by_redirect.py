'''
description:

In this example we use the openpay REST API
to create a charge to a card by redirection. 

We do not store card data, the user is paying directly in openpay website.

output:
status code: 200
{
   "id": "tr3nbzn5dgypqpqfeucb",
   "authorization": null,
   "operation_type": "in",
   "transaction_type": "charge",
   "status": "charge_pending",
   "conciliated": false,
   "creation_date": "2021-09-20T17:24:23-05:00",
   "operation_date": "2021-09-20T17:24:23-05:00",
   "description": "Cargo inicial a mi cuenta",
   "error_message": null,
   "order_id": "oid-002",
   "payment_method": {
      "type": "redirect",
      "url": "https://sandbox-api.openpay.mx/v1/mw31nv2zyvign0j9c7js/charges/tr3nbzn5dgypqpqfeucb/card_capture"
   },
   "amount": 2.22,
   "currency": "MXN",
   "customer": {
      "name": "Juan",
      "last_name": "Vazquez Juarez",
      "email": "juan.vazquez@empresa.com.mx",
      "phone_number": "4423456723",
      "address": null,
      "creation_date": "2021-09-20T17:24:21-05:00",
      "external_id": null,
      "clabe": null
   },
   "method": "card"
}



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
data = {
   "method"         : "card",
   "amount"         : 3.03,
   "description"    : "3 gorras adidas",
   "order_id"       : "oid-003",
   
   "customer"       : {
        "name"          : "Juan",
        "last_name"     : "Vazquez Juarez",
        "phone_number"  : "4423456723",
        "email"         : "juan.vazquez@empresa.com.mx"
   },

   "confirm"        : "false",
   "send_email"     : "false",
   "redirect_url"   : "http://www.openpay.mx/index.html"
}

headers = {'Content-type': 'application/json' }

# request charge
r = requests.post( url
    , data      = json.dumps( data )
    , headers   = headers
    , auth      = ( OPENPAY_PRIVATE_KEY, None ) )

# print response
print( 'status code: {}'.format( r.status_code ) ) 
print( json.dumps( r.json(), indent= 3 ) )

print(  '... end.' )
