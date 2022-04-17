'''

links:
https://docs.python.org/3/library/datetime.html

'''


from datetime import datetime
dt = datetime.now()

s = dt.isoformat()
print( '\n s: {}'.format( s ) )


format = '%Y %M %D %H:%M%:%S' # The format
dt2    = datetime.fromisoformat( s )
s2 = dt2.isoformat()

print ( 'dt2: {}'.format( dt2 ) )  
print ( 's2: {}'.format( s2 ) )  

print( '\n ... end.' )
