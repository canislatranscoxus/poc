from datetime import timedelta, date, datetime

d = date.today()
dt = datetime.now()

print( '\n current date, datetime' )
print( 'date: {}'.format( d.isoformat() ) )
print( 'datetime: {}'.format( dt.isoformat() ) )

end_date     = d + timedelta( days= 3 )
end_datetime = d + timedelta( days= 3 )

print( '\n after adding 3 days' )
print( 'end_date    : {}'.format( end_date.isoformat() ) )
print( 'end_datetime: {}'.format( end_datetime.isoformat() ) )

print( '\n'  )
