import unittest

class TestTrue( unittest.TestCase ):

    def test_true( self ):
        #self.assertTrue( True )
        self.assertTrue( 5 + 3 == 8 )

    def test_false( self ):
        #self.assertFalse( False )
        self.assertFalse( 5-0 == 3 )

if __name__ == '__main__':
    unittest.main()
