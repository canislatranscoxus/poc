from os import path
import qrcode
import qrcode.image.svg

# define a method to choose which factory metho to use
# possible values 'basic' 'fragment' 'path'
method = "SvgFillImage"

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
elif method == 'path':
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage
elif method == 'SvgFillImage':
    factory = qrcode.image.svg.SvgFillImage
else:    
    factory = qrcode.image.svg.SvgPathFillImage


# '07502307940070' 
data = "orandum est ut sit mens sana in corpore sano"

# Set data to qrcode
img = qrcode.make(data, image_factory = factory )


out_dir = '/home/art/tmp/codes/'
#file_name = 'barcode_1.svg'
file_name = 'qr_03.svg'
file_path = path.join( out_dir, file_name  )

# Save svg file somewhere
img.save( file_path )

