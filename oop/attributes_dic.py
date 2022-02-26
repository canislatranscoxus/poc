
from unicodedata import name
from xml.dom.domreg import well_known_implementations


class Robot:
    model       = None
    material    = None
    technology  = None

    def __init__( self, model, material, technology ) -> None:
        self.model       = model     
        self.material    = material  
        self.technology  = technology
        print( 'Robot created' )


r1 = Robot( 'T800', 'platinum', 'platinum recovered by live skin' )
r2 = Robot( 'T1000', 'liquid metal', '3D morphing' )

print( 'r1: {}'.format( r1.__dict__ ) )
print( 'r2: {}'.format( r2.__dict__ ) )