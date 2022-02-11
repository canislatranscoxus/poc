'''
Convert String  -> byte_array -> utf8 -> ascii
'''

s           = '\x80 😀 UTF-8 DATA'

#data        = b'\x80 \0xF0 UTF-8 DATA'
data = str.encode( s)

utf8_data   = data.decode( "utf-8", 'replace' )
ascii_data  = utf8_data.encode( "ascii","ignore" )

print( 's         : {}'.format( s          ) )
print( 'data      : {}'.format( data       ) )
print( 'utf8_data : {}'.format( utf8_data  ) )
print( 'ascii_data: {}'.format( ascii_data ) )
