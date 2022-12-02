'''
description: read a csv file, 
                count the number of instances per each word,
                and return a dictionary with the number of times each word occur.

'''

from pandas import *
 


def get_word_count( file_path, column_name ):
    try:
        data = read_csv( file_path )
        col  = data[ column_name ].tolist()
        d    = {}

        for line in col:

            # clean line
            line = line.lower()     \
                .replace( '\t', ' ' ) \
                .replace( '\r', ' ' ) \
                .replace( '\n', ' ' ) \
                .replace( '-' , ' ' ) \
                .replace( '?' , ' ' )           

            # remove spaces
            for i in range( 4, 0):
                s = ' ' * i
                line = line.replace( s, '' )

            # count tokens, words
            tokens = line.split( ' ' )
            for t in tokens:
                if t in d:
                    d[ t ] += 1
                else:
                    d[ t ] = 1
        
        return d

    except Exception as e:
        print( 'get_word_count, error: {}'.format( e ) )

 
 
 
# take as input word count dictionary, and return a sorted list of dictionaries.
# Sort Descending, from more popular to less popular word.
# example:
# 
# d = {  
#   'hello' : 2
#   'world' : 1
#   'cat'   : 3 }
#
# output is: 
# [ 
#   ('cat'   , 3 )
#   ('hello' , 2)
#   ('world' , 1)
# ] 
# 
#  
def get_popular_sort_by( d, desc = True ):

    try:
        a = []
        for k, v in d.items():
            t = ( k, v )
            a.append( t )

        a.sort( key = lambda x: x[ 1 ], reverse= desc )
        return a

    except Exception as e:
        print( 'get_popular_sort_by, error: {}'.format( e ) )
