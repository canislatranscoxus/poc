import json
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
            'description'   : 'El aceite de HEMP de cañamo',

            'sku'           : '07502307940032',
            'weight'        : 0.08,
            'width'         : 4,
            'height'        : 11,
            'length'        : 4
        }
        j = courier.add_product( p )
        print( json.dumps( j, indent = 3 ) )


if __name__ == '__main__':

    ut = Ut1()
    ut.t_03()

    print( 'test... end. \n' )