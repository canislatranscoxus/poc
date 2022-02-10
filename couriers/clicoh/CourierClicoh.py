import json
from ntpath import join
import os
import requests

from datetime import datetime
from ICourier import ICourier

class CourierClicoh( ICourier ):

    access_token  = None
    refresh_token = None

    def request_tokens( self ):
        # use the API to request Access Token and Refresh Token, and save them to redis.
        j = None
        try:
            url     = join( self.CLICOH_URL, 'token/' ) 
            headers = { 'Content-type'  : 'application/json'}
            #auth    = ( self.CLICOH_USER, self.CLICOH_PASS ) 
            data    = {
                        'username' : self.CLICOH_USER,
                        'password' : self.CLICOH_PASS,
                      }

            response = requests.post( url
                , data      = json.dumps( data )
                , headers   = headers
                #, auth      = auth 
                )

            j = response.json()
            self.access_token  = j[ 'access'  ]
            self.refresh_token = j[ 'refresh' ]
            print( json.dumps( j, indent = 3  ) )

        except Exception as e:
            print( 'CourierClicoh.request_tokens(), error: {}'.format( e ) )
            #j = None
        finally:
            return j

    '''def cache_tokens( self, params ):
        #save tokens to redis
        pass


    def get_tokens_from_redis( self, params ):
        #get tokens from redis
        pass'''

    def call_api( self, method, uri, data = None ):
        try:
            url     = join( self.CLICOH_URL, uri )
            j = {}
            i = 0
            while i < 2:
                i = i +1
                headers = { 'Content-type'  : 'application/json',
                            'Authorization' : 'Bearer {}'.format( self.access_token ) 
                          }

                if method == 'POST':
                    response = requests.post( url, headers = headers )
                else:
                    response = requests.get ( url, headers = headers )
                
                if response.status_code >= 400 and response.status_code < 500:
                    self.request_tokens()
                    continue

                j = response.json()
                break

            return j

        except Exception as e:
            print( 'CourierDebug.get_menu_rates(), ... {}'.format( e ) )
            raise

    
    def get_products( self ):
        try:
            uri = 'public/v1/products/'
            j = self.call_api( 'GET', uri )
            print( json.dumps( j ) )
            return j

        except Exception as e:
            print( 'CourierDebug.get_products(), ... {}'.format( e ) )
            raise


    def get_rates( self, params ):
        '''use the api and get the prices. The data usually is row and we need to parse and clean.'''

        # loop 2 times
        # call api
        # if token expired try again

        # read response

        # return values

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



    def __init__( self, params = None ):
        try:
           
            self.CLICOH_URL  = os.environ[ 'CLICOH_URL'  ]
            self.CLICOH_USER = os.environ[ 'CLICOH_USER' ]
            self.CLICOH_PASS = os.environ[ 'CLICOH_PASS' ]

            if params != None:
                self.access_token  = params[ 'access_token'  ]
                self.refresh_token = params[ 'refresh_token' ]

        except Exception as e:
            print( 'CourierClicoh.__init__(), error: {}'.format( e ) )
