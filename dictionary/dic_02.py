'''
Convert dictionary to list
'''

d = {
        'cat'   : 'Furious Claw', 
        'dog'   : 'Fang Fighter', 
        'fish'  : 'Goldy',        
        'turtle': 'Leo Ninja' }

print( '\n dictionary, key value pairs \n' )    

for k, v in d.items():
    print( 'key: {}, value: {}'.format( k, v ) )

a = [ x  for x in d.items() ]
print( 'List of tuples' )
print( a )

l =[]
[ l.extend([k,v]) for k,v in d.items() ]

print( 'list of items' )
print( l )

print( '\n end. \n' )    
