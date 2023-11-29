
class Animal:
    static_var = 'cat'

    def __init__(self):
        self.name = 'Kitty'
        self.age  = 1

a = Animal()
b = Animal()

print( 'Animal.static_var: {}'.format( Animal.static_var ) )
print( 'a.static_var: {}'.format( a.static_var ) )
print( 'b.static_var: {}'.format( b.static_var ) )

Animal.static_var = 'scorpion'
a.static_var = 'lynx'
b.static_var = 'wolf'

print( 'static var is class var. It is shared by all the instances.' )

print( 'Animal.static_var: {}'.format( Animal.static_var ) )
print( 'a.static_var: {}'.format( a.static_var ) )
print( 'b.static_var: {}'.format( b.static_var ) )

print( 'End.' )