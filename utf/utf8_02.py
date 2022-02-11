import unidecode

s           = '\x80 😀 à á ä UTF-8 DATA'
data        = unidecode.unidecode( s )
ascii_data  = data.encode( "ascii","replace" )

print( 's         : {}'.format( s          ) )
print( 'data      : {}'.format( data       ) )
print( 'ascii_data: {}'.format( ascii_data ) )
