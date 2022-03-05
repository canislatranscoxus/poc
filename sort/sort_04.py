'''
links:
https://www.kite.com/python/answers/how-to-sort-a-list-with-a-lambda-expression-in-python
'''

import json

file_path = '/home/art/git/poc/sort/data.json'

f = open( file_path )
# returns JSON object as
# a dictionary
data = json.load(f)
f.close()


print( '\n Sort a list of dictionaries \n' )
data.sort( key = lambda d: int( d[ 'price' ] ) )

for d in data:
    print( '{price} ; {desc}'.format( **d ) )


print( '\n create a new list with 2 attributes \n'  )
a = [ ( d[ 'price' ], d[ 'desc' ] ) for d in data  ]    
for tuple in a:
    print( tuple )