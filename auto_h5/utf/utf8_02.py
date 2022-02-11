s           = '\x80 😀 UTF-8 DATA'

#data        = b'\x80 \0xF0 UTF-8 DATA'
#data = str.encode( s)

#utf8_data   = data.decode( "utf-8", 'replace' )
ascii_data  = s.encode( "ascii","ignore" )

print( 's         : {}'.format( s          ) )
print( 'ascii_data: {}'.format( ascii_data ) )
