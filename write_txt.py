import datetime

file_path = '/home/art/tmp/a1.log'

s = '{} \n'.format( datetime.datetime.now() )
print( s )

with open( 'dog_breeds_reversed.txt', 'w') as writer:
    writer.write( s )
    writer.write( 'hello hip hop dancers' )
 