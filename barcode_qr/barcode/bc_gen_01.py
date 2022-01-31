'''
description: This code generate an SVG image for a string barcode.

links:
    https://www.geeksforgeeks.org/how-to-generate-barcode-in-python/
    https://python-barcode.readthedocs.io/en/stable/barcode.html
'''

from os import path

# import EAN13 from barcode module
from barcode import EAN13


# Make sure to pass the number as string
number = '5901234123457'

  
# Now, let's create an object of EAN13
# class and pass the number
my_code = EAN13(number)

out_dir = '/home/art/tmp/codes/'
file_name = 'barcode_1.svg'
file_path = path.join( out_dir, file_name  )

# Our barcode is ready. Let's save it.
my_code.save( file_path )
