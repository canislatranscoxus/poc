# Get a string from  a number in currency format. 
# Currency symbol $, thousand separator, decimal separator, and
# two decimal places

my_numbers = [
    123,
    12345678910.987654,
    345678910.91234,    
    987654
]

print( '\n two decimals and round format \n' )
for i in my_numbers:
    print( '${:0,.2f}'.format( i ) )


print( '\n Python decimal format \n' )
for i in my_numbers:
    print( '${0:0,.3g}'.format( i ) )

print( '\n Limiting floats to two decimal points \n' )
for i in my_numbers:
    my_float = round(i , 2)
    print( '${:0,.2f}'.format( my_float ) )

