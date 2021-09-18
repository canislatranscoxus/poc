'''
description:

in this example we will use a sandbox environment,
and make a charge to a testing card.

enjoy it

links:
https://github.com/open-pay/openpay-python

https://github.com/canislatranscoxus/poc


'''


import openpay
import os

# set initial parameters

#os.environ[ 'OPENPAY_PUBLIC_KEY' ]
#os.environ[ 'OPENPAY_URL'        ]


openpay.merchant_id         = os.environ[ 'OPENPAY_MERCHANT_ID' ]
openpay.api_key             = os.environ[ 'OPENPAY_PRIVATE_KEY' ]
openpay.verify_ssl_certs    = False
openpay.production          = False  # By default this works in sandbox mode
openpay.country             = 'mx'  # 'mx' is default value, to use for Colombia set country='co'

# create token
openpay.Token.create(
    card_number="4111111111111111",
    holder_name="Juan Perez Ramirez",
    expiration_year="20",
    expiration_month="12",
    cvv2="110",
    address={
        "city": "Querétaro",
        "country_code": "MX",
        "postal_code": "76900",
        "line1": "Av 5 de Febrero",
        "line2": "Roble 207",
        "line3": "col carrillo",
        "state": "Queretaro"
    })

# create a new user
customer = openpay.Customer.create(
    name="Juan",
    email="somebody@example.com",
    address={
        "city": "Queretaro",
        "state": "Queretaro",
        "line1": "Calle de las penas no 10",
        "postal_code": "76000",
        "line2": "col. san pablo",
        "line3": "entre la calle de la alegria y la calle del llanto",
        "country_code": "MX"
    },
    last_name="Perez",
    phone_number="44209087654"
)

print( customer )


# get a customer
customer_id = 'amce5ycvwycfzyarjf8l'
customer = openpay.Customer.retrieve( customer_id  )











