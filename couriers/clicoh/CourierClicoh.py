
from dataclasses import dataclass
import json
import os
import requests

from datetime import datetime
from ICourier import ICourier

class CourierClicoh( ICourier ):

    def request_tokens( self, params ):
        # use the API to request Access Token and Refresh Token, and save them to redis.
        try:
            url     = self.CLICOH_URL
            headers = {'Content-type': 'application/json' }
            auth    = ( self.OPENPAY_PRIVATE_KEY, None ) 
            data    = {
                        'username' : self.CLICOH_USER,
                        'password' : self.CLICOH_PASS,
                      }

            response = requests.post( self.url
                , data      = json.dumps( data )
                , headers   = self.headers
                , auth      = self.auth )

            j = json.loads( response )
            print( json.dumps( response, indent = 3  ) )


            return response



        except Exception as e:
            print( 'request_tokens().' )

    def get_tokens( self, params ):
        #get tokens from redis
        pass

    def get_

    def get_at( self, params ):
        pass


    def get_rates( self, params ):
        '''use the api and get the prices. The data usually is row and we need to parse and clean.'''
        pass

    def get_menu_rates( self, params ):
        ''' Get the rates from the courier and clean the data to be ready to use in a
        radio button menu in a web page. The output is a dictionary
        { 
            rate_id : { 
                        'desc'      : ...,
                        'price'     : ...,
                        'courier'   : ...,
                      }
            .
            .
            .
        }
        '''
        try:
            d = {
                'dhl001' : { 'desc': 'DHL 1 day  $100.00',  'service' : 'DHL Express' , 'price': 100.00 , 'courier' : 'DHL', 'arriving_time': '1 day' , 'courier_class': self.__class__.__name__ } ,
                'dhl002' : { 'desc': 'DHL 3 days $ 50.00',  'service' : 'DHL Regular' , 'price':  50.00 , 'courier' : 'DHL', 'arriving_time': '3 days', 'courier_class': self.__class__.__name__ } ,
                'ups001' : { 'desc': 'UPS 1 day  $ 99.00',  'service' : 'UPS Critical', 'price':  99.00 , 'courier' : 'UPS', 'arriving_time': '1 day' , 'courier_class': self.__class__.__name__ } ,
                'ups002' : { 'desc': 'UPS 3 days $ 47.00',  'service' : 'UPS domestic', 'price':  47.00 , 'courier' : 'UPS', 'arriving_time': '3 days', 'courier_class': self.__class__.__name__ } ,
            }
            return d
        except Exception as e:
            print( 'CourierDebug.get_menu_rates(), ... {}'.format( e ) )
            raise
        

    def create_shipment( self, params ):
        try:
            self.create_tracking_number( params )

            response = { 
                'tracking_number' : self._tracking_number
            }

            return response

        except Exception as e:
            print( 'CourierDebug.create_shipment(), error: {}'.format( e ) )
 
        

    def create_tracking_number( self, params ):
        '''Crear guia'''
        self._tracking_number = datetime.now().isoformat( timespec= 'seconds' )



    def __init__( self, params=None ):
        if params == None:
            self.CLICOH_URL  = os.environ[ 'CLICOH_URL'  ]
            self.CLICOH_USER = os.environ[ 'CLICOH_USER' ]
            self.CLICOH_PASS = os.environ[ 'CLICOH_PASS' ]
        else:
            self.CLICOH_URL  = params[ 'CLICOH_URL'  ]
            self.CLICOH_USER = params[ 'CLICOH_USER' ]
            self.CLICOH_PASS = params[ 'CLICOH_PASS' ]

