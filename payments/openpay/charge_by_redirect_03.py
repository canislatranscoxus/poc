'''
description:

In this example we use the openpay REST API
to create a charge to a card by redirection. 

We do not store card data, the user is paying directly in openpay website.

output:

{
   "id": "trv4dud3bxjcfa2rtsfq",
   "authorization": null,
   "operation_type": "in",
   "transaction_type": "charge",
   "status": "charge_pending",
   "conciliated": false,
   "creation_date": "2021-11-19T18:03:57-06:00",
   "operation_date": "2021-11-19T18:03:57-06:00",
   "description": "Paquete Piel Joven hemp",
   "error_message": null,
   "order_id": "ov-nov19-001",
   "payment_method": {
      "type": "redirect",
      "url": "https://sandbox-api.openpay.mx/v1/mw31nv2zyvign0j9c7js/charges/trv4dud3bxjcfa2rtsfq/card_capture"
   },
   "amount": 369.43,
   "currency": "MXN",
   "customer": {
      "name": "Merida",
      "last_name": "Brave Scarlett",
      "email": "merida.brave@gmail.com",
      "phone_number": "12345678",
      "address": null,
      "creation_date": "2021-11-19T18:03:57-06:00",
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
   "method": "card", 
   "amount": 944.0, 
   "description": "Oasisverde", 
   "order_id": "local_nov22_0955_03", 

   "customer"       : {
        "name"          : "Snoop",
        "last_name"     : "Dogg",
        "phone_number"  : "6633 9933",
        "email"         : "snoop.dogg@gmail.com"
   },

   "confirm": "false", 
   "send_email": "false", 
   #"redirect_url": "https://127.0.0.1:8000/" # fail

   "redirect_url"   : "http://www.basmatiyes.com"  # OK
   #"redirect_url"   : "http://www.openpay.mx/index.html"  # OK
}


headers = {'Content-type': 'application/json' }
auth      = ( OPENPAY_PRIVATE_KEY, None )

print( 'url     :{}'.format( url     ) )
print( 'headers :{}'.format( headers ) )
print( 'auth    :{}'.format( auth    ) )


# request charge
r = requests.post( url
    , data      = json.dumps( data )
    , headers   = headers
    , auth      = ( OPENPAY_PRIVATE_KEY, None ) )

# print response
print(  '\n ... response \n' )
print( 'status code: {}'.format( r.status_code ) ) 

print(  '\n' )
print( json.dumps( r.json(), indent= 3 ) )
print(  '\n ... end.' )
