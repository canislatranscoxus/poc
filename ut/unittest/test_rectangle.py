import unittest
import sys
from rectangle_perimeter import get_perimeter

class TestRectangle( unittest.TestCase ):

    def test_perimeter( self ):
        self.assertEqual( 30, get_perimeter( 10, 5 ) )
    
    @unittest.skip( 'Temporary skip this test' )
    def test_error( self ):
        self.assertRaises( 
            ValueError, 
            get_perimeter, 
            10, 0 )
            #10, 5 )
        
    @unittest.skipIf( sys.version_info.major == 3, 'This is python 3' )
    def test_error2( self ):
        with self.assertRaises( ValueError ):
            get_perimeter(10, 0)


    @unittest.skipUnless( sys.platform.startswith( 'wind' ), 'This test requires Windows' )
    def test_win( self ):
        self.assertEqual( 1, 1 )


if __name__ == '__main__':
    unittest.main()

