from io import BytesIO
bytesio_object = BytesIO(b"Hello World!")

# Write the stuff
file_path = '/home/art/tmp/bytes_2_file.txt'

with open( file_path, "wb") as f:
    f.write(bytesio_object.getbuffer())

print( '\n ... end.  \n' )
