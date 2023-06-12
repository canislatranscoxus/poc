'''
A Generator is a function that return an iterator
'''


def my_generator(  ):
    n = 0

    n = n + 1
    yield n

    n = n + 2
    yield n

    n = n + 3
    yield n


g = my_generator()

s1 = next( g )
s2 = next( g )
s3 = next( g )


print( 's1: {}', s1  )
print( 's2: {}', s2  )
print( 's3: {}', s3  )

