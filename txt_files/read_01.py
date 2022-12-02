'''
description: read a txt file, and print to console each word
'''

in_file_path  = '/home/art/git/poc/txt_files/p1.txt'

# dictionary of words
d = {}

a = []

with open( in_file_path, 'r') as reader:
   
    lines = reader.readlines()
    for line in lines:
        print ( line )

        line = line.replace( '\t', ' ' )    \
            .replace( '\r', ' ' )           \
            .replace( '\n', ' ' )           \
            .replace( '?' , ' ' )           


        for i in range( 4, 0):
            s = ' ' * i
            line = line.replace( s, '' )

        tokens = line.split( ' ' )
        for t in tokens:
            if t in d:
                d[ t ] += 1
            else:
                d[ t ] = 1
                a.append( t )

a.sort()
    
print( '\n Dictionary, word count \n' )
for k, v in d.items():
    print( '{}: {}'.format( k, v )  )

print( '\n sorted words \n' )
for word in a:
    print( word )

print( '\n end. \n' )
 