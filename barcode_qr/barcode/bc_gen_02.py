'''
description: This code generate an SVG image for a string barcode.

links:
    https://www.geeksforgeeks.org/how-to-generate-barcode-in-python/
    https://python-barcode.readthedocs.io/en/stable/barcode.html
'''

from os import path
# import EAN13 from barcode module
import barcode
from barcode import EAN13
  
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter
  
# Make sure to pass the number as string
number = '5901234123457'
  
# Now, let's create an object of EAN13 class and 
# pass the number with the ImageWriter() as the writer


ean = barcode.get( 'ean13', '123456789102', writer=ImageWriter())
ean.save( 'ean13' )


my_code = EAN13(number, writer=ImageWriter())

out_dir = '/home/art/tmp/codes/'
file_name = 'barcode_2.png'
file_path = path.join( out_dir, file_name  )

# Our barcode is ready. Let's save it.
my_code.save( file_path )


