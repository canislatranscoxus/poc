import datetime

file_path = '/home/art/tmp/dogs.txt'

s = '{} \n'.format( datetime.datetime.now() )
print( s )

with open( file_path, 'w') as writer:
    writer.write( 'pit bull\n'    )
    writer.write( 'akita inu\n'   )
    writer.write( 'malamut\n'     )
    writer.write( 'dogo brasileiro\n' )
    writer.write( 'mastin\n'      )

 