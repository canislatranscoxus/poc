
# create instance using a string of Class Name

class Cat:
    def hello( self ):
        print( 'Miew, I am a cat' )

class Dog:
    def hello( self ):
        print( 'Barf, I am a dog' )        


class_name = 'Cat'
klass   = globals()[ class_name ]
kity = klass()
kity.hello()

class_name = 'Dog'
klass   = globals()[ class_name ]
spike = klass()
spike.hello()