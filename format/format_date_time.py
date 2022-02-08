'''

links:
https://docs.python.org/3/library/datetime.html

'''


from datetime import datetime
dt = datetime.now()

s = dt.isoformat()
print( s )

s = dt.isoformat( timespec= 'seconds' )
print( s )