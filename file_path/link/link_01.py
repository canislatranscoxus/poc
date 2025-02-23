'''
Create a symbolic link for 1 file
'''

import os

src = '/home/art/tmp/a/011524/ant.dat'
tar = '/home/art/tmp/a/011524/ant_link.txt'

os.symlink( src, tar )

print( 'end.' )
