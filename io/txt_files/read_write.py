'''
description: read a txt file, clean the data and write it to another txt file.
'''

from asyncore import read
import datetime

#in_file_path  = '/home/art/tmp/sql/insert_product.sql'
#out_file_path = '/home/art/tmp/sql/pretty_01.sql'

in_file_path  = '/home/art/tmp/sql/cbd_dev_01_shop_product_translation.sql'
out_file_path = '/home/art/tmp/sql/pretty_02.sql'

raw_data = None


with open( in_file_path, 'r') as reader:
    raw_data = reader.read()

clean_data = raw_data.replace( '),(', '),\n(' )

with open( out_file_path, 'w') as writer:
    writer.write( clean_data )

print( '\n output file: {}'.format( out_file_path ) )
print( 'pretty file created! \n' )
 