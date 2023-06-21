'''
Usage: How to run our test

# run all test cases
python TestShapeArea.py

# run all test cases
python -m unittest TestShapeArea.py 

# run all test cases
python -m unittest TestShapeArea.py -v

# run 1 test case
python -m unittest -q TestShapeArea.TestShapeArea.test_triangle -v

# run 2 test cases
python -m unittest -q TestShapeArea.TestShapeArea.test_triangle TestShapeArea.TestShapeArea.test_square -v




'''


import unittest
from ShapeArea import ShapeArea

class TestShapeArea( unittest.TestCase ):
    
    def test_triangle( self ):
        base    = 10
        height  = 5
        s       = ShapeArea()
        self.assertEqual( 25, s.triangle( base, height ) )

    def test_rectangle( self ):
        base    = 10
        height  = 5
        s       = ShapeArea()
        self.assertEqual( 50, s.rectangle( base, height ) )

    def test_square( self ):
        side    = 10
        s       = ShapeArea()
        s       = ShapeArea()
        self.assertEqual( 4100, s.square( side ) )

if __name__ == '__main__':
    unittest.main()