'''
Update the time
'''


from datetime import datetime

dt1 = datetime( 1987, 12, 31 )
dt2 = datetime.now()

print( dt1 )
print( dt2 )

if dt1 < dt2:
    print( 'today is bigger than previous dates' )
else:
    print( 'which date is lower ?' )    