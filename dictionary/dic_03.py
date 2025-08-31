'''
Convert dictionary to list
'''

def get_animal( d ):
    try:
        d[ 'cat' ] = 'Furious Claw'
        d[ 'dog' ] = 'Fang Fighter'
        d[ 'fish'] = 'Goldy'
        d[ 'turtle'] = 'Leo Ninja'

        return 'cat'
    except Exception as e:
        print( 'error: {}'.format( 'get_animal' ) )

d = {}

animal = get_animal( d )

print( animal )
print( d )
