

def get_perimeter( width, height ):
    if width == 0 or height == 0:
        raise ValueError( 'Invalid Input! ' )

    p = ( width + height ) * 2
    return p

