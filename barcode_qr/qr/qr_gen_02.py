from os import path
import qrcode

img = qrcode.make( '07502307940070' )
type(img)  # qrcode.image.pil.PilImage

out_dir = '/home/art/tmp/codes/'
#file_name = 'barcode_1.svg'
file_name = 'qr_02.png'
file_path = path.join( out_dir, file_name  )


img.save( file_path )

