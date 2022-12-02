'''
description: read a txt file, and print to console each word
'''
from os.path import join
from word_count import *


my_dir    = '/home/art/Downloads/s_frog/hempmeds/'
file_col = [ 
    [ 'titles.csv'  , 'Title 1' ],
    #[ 'h1.csv'      , 'H1-1'    ],
    #[ 'h2.csv'      , 'H2-1'    ],
    #[ 'meta_description.csv', 'Meta Description 1'],
    #[ 'internal.csv', '' ],    
]

for i in file_col:
    file_path  = join( my_dir, i[ 0 ] )
    d = get_word_count( file_path, i[ 1 ] )

   
    print( '\n {}, word count \n'.format( i[0] ) )
    for k, v in d.items():
        print( '{}: {}'.format( k, v )  )


    a = get_popular_sort_by( d )
    for i in a:
        print( i )



print( '\n end. \n' )
 