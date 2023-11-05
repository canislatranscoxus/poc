# get the directory and file name from path

import os

my_file_path = '/home/folder_a/folder_b/folder_c/animals.txt'

dir, file_name = os.path.split( my_file_path )

print( 'dir      : {}'.format( dir       ) )
print( 'file_name: {}'.format( file_name ) )

