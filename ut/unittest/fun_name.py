import unittest

import triangle_area 

class Test( unittest.TestCase ):

    ''' 
    # we can override runTest() method

    def runTest( self ):
        result = triangle_area.triangle( 10, 5 )
        self.assertEqual( result, 25 )
    '''

    def triangle_test( self ):
        result = triangle_area.triangle( 10, 5 )
        self.assertEqual( result, 25 )


if __name__ == '__main__':
    unittest.main()


