'''
Update the time
'''


from datetime import datetime, timedelta

dt = datetime.now()

two_hours_from_now = dt + timedelta(hours= 2)

print( dt )
print( two_hours_from_now )

