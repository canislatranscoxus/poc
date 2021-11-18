from datetime                   import date, timedelta

week_days = [
'Domingo',        
    'Lunes',
    'Martes',
    'Miércoles',
    'Jueves',
    'Viernes',
    'Sábado',
    
]

today   = date.today()
#my_date = today + timedelta( days = 3 )
my_date = today 





i = 0
day = int( my_date.strftime( '%w' ) )
dow = week_days[ day ]
txt = 'Day of week is: {} * {}'.format( day, dow )

print( '\n', txt, '\n' )
