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

#field = 'price'
field = 'arriving_time'
s = '{' + field + '}' + ';' +  '{desc}'

data.sort( key = lambda d: int( d[ field ] ) )

for d in data:
    
    print( s.format( **d ) )