import json
import os
import requests
import unidecode
from os.path    import join
from datetime   import datetime

from ICourier   import ICourier

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
            #print( json.dumps( j, indent = 3  ) )

        except Exception as e:
            print( 'CourierClicoh.request_tokens(), error: {}'.format( e ) )
            #j = None
        finally:
            return j

    def call_api( self, method, uri, data = None ):
        status_code = ''
        try:
            url     = join( self.CLICOH_URL, uri )
            j = {}
            i = 0
            
            if self.access_token == None:
                self.request_tokens()

            while i < 2:
                i = i +1
                headers = { 'Content-type'  : 'application/json',
                            'Authorization' : 'Bearer {}'.format( self.access_token ) 
                          }

                if method == 'POST':
                    response = requests.post( url, headers = headers, data = json.dumps( data ) )
                else:
                    response = requests.get ( url, headers = headers, data = json.dumps( data ) )

                if response.status_code >= 400 and response.status_code < 500:
                    self.request_tokens()
                    continue

                j = response.json()
                break

            j[ 'status_code' ] = response.status_code
            return j

        except Exception as e:
            print( 'CourierDebug.get_menu_rates(), ... {}'.format( e ) )
            raise



    def utf8_to_ascii( self, utf8_string ):
        # remove accents
        data        = unidecode.unidecode( utf8_string )
        ascii_data  = data.encode( "ascii","replace" )
        return data
    

    def get_products( self ):
        try:
            uri = 'public/v1/products/'
            j = self.call_api( 'GET', uri )
            #print( json.dumps( j ) )
            return j

        except Exception as e:
            print( 'CourierDebug.get_products(), ... {}'.format( e ) )
            raise

    def add_product( self, product ):
        try:
            uri = 'public/v1/products/'
            data =  {
                "name"          : self.utf8_to_ascii( product[ 'name' ] ),
                "description"   : self.utf8_to_ascii( product[ 'description' ][:150] ),
                "variants"      : [
                    {
                        "sku"       : product[ 'sku' ],
                        "is_active" : 'true',
                        "variant"   : {
                            "weight"    : product[ 'weight' ],
                            "width"     : int( product[ 'width'  ] ),
                            "height"    : int( product[ 'height' ] ),
                            "length"    : int( product[ 'length' ] )
                        }
                    }
                ]
            }

            #print( json.dumps( data, indent = 3 ) )    
            j = self.call_api( 'POST', uri, data )
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
