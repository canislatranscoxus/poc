
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

print( '\n get Object Attributes in a Dictionary' )
print( 'r1: {}'.format( r1.__dict__ ) )
print( 'r2: {}'.format( r2.__dict__ ) )

print( '\n get the class name from the Object' )
print( 'object: r1, type:{} ,Class Name: {}'.format( type(r1), type(r1).__name__ ) )
print( 'object: r1, type:{} ,Class Name: {}'.format( type(r1), type(r1).__name__ ) )

print( '\n\n' )