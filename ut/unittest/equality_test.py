import unittest

class TestEquality( unittest.TestCase ):

    def test_true( self ):
        self.assertEqual( 8, 5 + 3 )

    def test_false( self ):
        self.assertNotEqual( 5-0, 3 )

if __name__ == '__main__':
    unittest.main()
