from CourierClicoh import CourierClicoh


class Ut1:

    def t_01( self ):
        # Test get access token and refres token
        courier = CourierClicoh()
        courier.request_tokens()

    def t_02( self ):
        # Test get products
        courier = CourierClicoh()
        courier.get_products()



if __name__ == '__main__':

    ut = Ut1()
    ut.t_02()

    print( 'test... end. \n' )