# Python unittest

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