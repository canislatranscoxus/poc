'''
description: we extract the price from some text
'''

import re

print( '\n Extract the price. The numbers can contain commas, and can have decimals with one or two digits. \n' )

#pattern = '\$?((\d{1,3}(\,){0,1})*\d{1,3}\.\d{1,2})'
#pattern = '\$?((\d{1,3}(\,){0,1})*\d{1,3}\.\d{1,2})'
pattern = '\$(\s){0,1}\d{1,3}'

prog = re.compile( pattern )



a = [
    '$ 123,456,678.00 MNX dhl express',
    '$ 123,456,678.00 MNX dhl regular 3 days',
    '$123,456,678.0 MNX ups Fast mode',
    '$123,456,678.00 MNX ups domestic',
    '$123456678.00 MNX ups domestic',
]

for i in a:
    #result = prog.match( i )
    result = re.match( pattern, i )

    print( '\n' )
    print( result )
    if result != None:
        print( result.group( 0 ) )


print( '\n End.' )    