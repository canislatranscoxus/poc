'''
description: This class wraps the openpay charges functionality.
             Here we request a charge by redirection, and get list of charges.
             Behind the scenes we call openpay API.

links:
    https://www.openpay.mx/docs/op-form-charge.html
    https://www.openpay.mx/api/?shell#con-redireccionamiento
    https://www.openpay.mx/docs/testing.html
    https://www.openpay.mx/api/?shell#listado-de-cargos
'''

import json
import os
import requests


class Charges:
    OPENPAY_URL         = None
    OPENPAY_MERCHANT_ID = None
    OPENPAY_PRIVATE_KEY = None

    url     = None
    headers = None
    auth    = None

    def request_bank_ref( self, data ) :
        response = requests.post( self.url
            , data      = json.dumps( data )
            , headers   = self.headers
            , auth      = self.auth )

        return response


    def request_redirect_charge( self, data ):
        '''request to openpay site a link to make a charge by redirection.
        If everything looks ok, 
            we get a response with status 200 and a json 
            with the link to redirect our client to pay.
        else,
            we get an error status, and error mesagge in json.
        
        data: This is a json with all the parameters we need, for example: order-id,
        customer, payment type, amount, currency, ...

        '''
        response = requests.post( self.url
            , data      = json.dumps( data )
            , headers   = self.headers
            , auth      = self.auth )

        return response

    def get_all( self ):
        response = requests.get( self.url
        , headers   = self.headers
        , auth      = self.auth )
        return response

    def get_list_where( self, params=None ):
        '''get the list of charges, using the params as filter.

        params: json. It is a dictionary that contain all the parameters used in the filter.
                It has the next structure

        params = {
        'order_id'      :
        'creation'      :
        'creation[gte]' :
        'creation[lte]' :
        'offset'        :
        'limit'         :
        'amount'        :
        'amount[gte]'   :
        'amount[lte]'   :
        'status'        :        
        }'''

        if params == None:
            response = requests.get( self.url
            , headers   = self.headers
            , auth      = self.auth )
        else:
            response = requests.get( self.url
            , params    = params
            , headers   = self.headers
            , auth      = self.auth )
        
        return response


    def get_list( self, order_id ):
        ''' get the list of charges filtering by one order_id. '''

        params = {
            'order_id'       : str(order_id),
        }
        response = self.get_list_where( params )
        return response

    def get_charge( self, order_id ):
        ''' get the first charge (from openpay )of order_id'''
        charges     = Charges()        
        status= None
        try:
            orders      = charges.get_list( order_id )
            j = orders.json()
            return j[ 0 ]
        except Exception as e:
            print( 'payment.openpay.Charges.get_charge(), error: {}'.format( e ) )
            return None            




    def __init__( self, params=None ):
        if params == None:
            self.OPENPAY_URL         = os.environ[ 'OPENPAY_URL'         ]
            self.OPENPAY_MERCHANT_ID = os.environ[ 'OPENPAY_MERCHANT_ID' ]
            self.OPENPAY_PRIVATE_KEY = os.environ[ 'OPENPAY_PRIVATE_KEY' ]
        else:

            self.OPENPAY_URL         = params[ 'OPENPAY_URL'         ]
            self.OPENPAY_MERCHANT_ID = params[ 'OPENPAY_MERCHANT_ID' ]
            self.OPENPAY_PRIVATE_KEY = params[ 'OPENPAY_PRIVATE_KEY' ]

        self.url     = '{}{}/charges'.format( self.OPENPAY_URL, self.OPENPAY_MERCHANT_ID )
        self.headers = {'Content-type': 'application/json' }
        self.auth    = ( self.OPENPAY_PRIVATE_KEY, None ) 