'''
here we use arg list as parameters of a function
'''

def bring_pets( location, *animals ):
    
    print( '\n we are in {}'.format( location ) )
    
    for i in animals:
        print( i )



# testing with an array
location = 'the snowy mountain'
a = [ 'dog', 'cat', 'turttle' ]
bring_pets( location, *a )

# testing with a multiple strings in the parameters
location = 'the snowy mountain'
bring_pets( location, 'centipod', 'mangost', 'wolfverine' )


print( '\n.... end.' )