'''
2. Hacer un programa q diga si el string es un usuario AMERICAS, XYZ, email (tienen arroba @ ) o apellido.
ejemplo:

usuarios de AMERICAS:
    AMERICAS_maria
    AMERICAS_pedro
    AMERICAS_lupita
    emea_abdul

usuarios XYZ:
    XYZ_cat
    XYZ_dog
    XYZ_fish

usuarios q entran con email:
    mickey@disney.com
    daisy@duck.net
    mini@toys.org
    donald@fun.club

usuarios q entran con su apellido:
    galindo
    perez
    garza
    garcia

'''

'angel a@amazon.com 1234567890 flag01 0x016'

user = input( 'teclee su user: ' )


if user.startswith( 'AMERICAS_' ) or user.startswith( 'emea_' ):
    print( 'su user es de AMERICAS' )

elif user.startswith( 'XYZ_' ):
    print( 'su user es XYZ' )

elif '@' in user:
    print( 'su user es un email' )

else:
    print( 'su user es un apellido' )

s = 'manzana mandarina pera piña'
frutas = s.split(  )
print( frutas )