d1 = { 'cat'  : 'Furious Claw', 'dog'   : 'Fang Fighter' }
d2 = { 'fish' : 'Goldy',        'turtle': 'Leo Ninja' }
d3 = {}
d4 = None

print( '\n Method 1. dict.update( d ) \n' )
result = {}
result.update( d1 )
result.update( d2 )
result.update( d3 )
# result.update( d4 ) # None dictionary causes Error
print( result  )

print( '\n Method 2. { **d1, **d2, ...  } \n' )
result = {
          **d1,
          **d2,
          **d3,
          #**d4, # None dictionary causes Error
         }
# result.update( d4 ) # None dictionary causes Error
print( result  )


print( '\n Method 3. Pipe  d1 | d2 |...  } \n' )
result = d1 |d2 | d3 
        # | d4  # None dictionary causes Error
print( result  )