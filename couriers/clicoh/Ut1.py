import json
from os.path import join
import os
import requests

from datetime import datetime


from CourierClicoh import CourierClicoh


class Ut1:

    def t_01( self ):
        # Test get access token and refres token
        courier = CourierClicoh()
        courier.request_tokens()

    def t_02( self ):
        # Test get products
        courier = CourierClicoh()
        j = courier.get_products()
        print( '\n', json.dumps( j, indent = 3 ) )

    def t_03( self ):
        # Test add products
        courier = CourierClicoh()
        p = {
            'name'          : 'Gotero de CBD 500mg',
            'description'   : 'El aceite de HEMP de canamo',

            'sku'           : '07502307940032',
            'weight'        : 0.08,
            'width'         : 4,
            'height'        : 11,
            'length'        : 4
        }
        j = courier.add_product( p )
        print( json.dumps( j, indent = 3 ) )

    def t_04( self ):
        # add product
        try:
            courier = CourierClicoh()
            courier.request_tokens()

            my_data = {"name" : "Gorra Azul",
                "description"   : "Gorra azul de algodon",
                "variants"      : [ 
                {
                    "sku"           : "07502307940032",
                    "is_active": "true",
                    "variant": {
                        "weight"        : 0.08,
                        "width"         : 4,
                        "height"        : 11,
                        "length"        : 4
                    }
                } ]
            }

            url = 'https://sandbox-api.clicoh.com/api/public/v1/products/'
            headers = { 'Content-Type'  : 'application/json',
                        #Content-Type: application/json
                        'Authorization' : 'Bearer {}'.format( courier.access_token ) 
                      }
            response = requests.post( url, headers = headers, data = json.dumps( my_data ) )
            print( response.status_code )
            j = response.json()
            print( json.dumps( j, indent = 3 ) )

        except Exception as e:
            print( 'CourierDebug.get_menu_rates(), ... {}'.format( e ) )
            raise



if __name__ == '__main__':

    ut = Ut1()
    ut.t_02()
    ut.t_03()

    print( 'test... end. \n' )