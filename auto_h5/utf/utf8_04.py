import unidecode

def utf8_to_ascii( utf8_string ):
    # remove accents
    data        = unidecode.unidecode( utf8_string )
    ascii_data  = data.encode( "ascii","replace" )
    return ascii_data


s           = '\x80 😀 à á ä UTF-8 DATA'
ascii_data = utf8_to_ascii( s )

print( 's         : {}'.format( s          ) )
print( 'ascii_data: {}'.format( ascii_data ) )
