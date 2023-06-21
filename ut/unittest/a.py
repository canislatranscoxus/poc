import unittest

class Testing( unittest.TestCase ):

    def test_string( self ):
        x = 'kitty'
        y = 'kitty'

        self.assertEqual( x, y )

if __name__ == '__main__':
    unittest.main()