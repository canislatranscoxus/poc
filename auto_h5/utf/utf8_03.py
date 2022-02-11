from unicodedata import normalize

s           = '\x80 😀 à á ä UTF-8 DATA'
data        = normalize( 'NFD', s )


print( 's         : {}'.format( s          ) )
print( 'data      : {}'.format( data       ) )

