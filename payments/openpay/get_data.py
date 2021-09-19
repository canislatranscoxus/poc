
import openpay
import os

# set initial parameters
openpay.merchant_id         = os.environ[ 'OPENPAY_MERCHANT_ID' ]
openpay.api_key             = os.environ[ 'OPENPAY_PRIVATE_KEY' ]
openpay.verify_ssl_certs    = False
openpay.production          = False  # By default this works in sandbox mode
openpay.country             = 'mx'  # 'mx' is default value, to use for Colombia set country='co'


# get all customers
customers = openpay.Customer.all()

for customer in customers:
    print( customer )


# get a customer
customer_id = 'amce5ycvwycfzyarjf8l'
customer = openpay.Customer.retrieve( customer_id  )

