'''
A Generator is a function that return an iterator
'''


def my_generator():
    print( '1. cat' )
    yield '1 is cat'

    print( '2. dog' )
    yield '2 is dog'

    print( '3. turttle' )
    yield '3 is turttle'

g = my_generator()

s1 = next( g )
s2 = next( g )
s3 = next( g )


print( 's1: {}', s1  )
print( 's2: {}', s2  )
print( 's3: {}', s3  )

