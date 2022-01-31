import qrcode
img = qrcode.make( 'We like wild animals' )
type(img)  # qrcode.image.pil.PilImage
img.save( "qr_01.png" )

