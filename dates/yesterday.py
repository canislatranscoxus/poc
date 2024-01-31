'''
Update the time
'''

from datetime import datetime, timedelta

dt = datetime.now()

print( dt )

print( "let's change hours: minutes : seconds" )

dt2 = dt.replace(hour=11, minute=59, second=59, microsecond=0 )
print( dt2 )


yesterday = datetime.combine(
    datetime.today() - timedelta(1),
    datetime.min.time())

print( 'yesterday midnight  ' ,yesterday )

