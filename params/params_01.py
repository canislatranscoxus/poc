def my_fun( animal: str ) -> str:
    txt = 'your pet is a {}'.format( animal )
    print( txt, '\n' )

def my_fun2( animal:  str = 'dog' ) -> str:
    txt = 'your pet is a {}'.format( animal )
    print( txt, '\n' )


my_fun( 'cat' )    
my_fun2(  )    