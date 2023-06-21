import unittest

class Testing( unittest.TestCase ):

    def test_upper( self ):
        self.assertEqual( 'beta'.upper(), 'BETA' )

    def test_bool( self ):
        x = True
        y = False
        self.assertEqual( x, y )

    def test_int( self ):
        x = 1
        y = 1
        self.assertEqual( x, y )

if __name__ == '__main__':        
    unittest.main()


