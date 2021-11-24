import redis
import os
import sys

REDIS_HOST = os.environ[ 'REDIS_HOST' ]
REDIS_PORT = os.environ[ 'REDIS_PORT' ]
#REDIS_DB   = os.environ[ 'REDIS_DB'   ]
REDIS_DB   = 0
REDIS_AUTH = os.environ[ 'REDIS_AUTH' ]


# connect to redis
r = redis.Redis( host     = REDIS_HOST
                ,port     = REDIS_PORT
                ,db       = REDIS_DB
                #,password = REDIS_AUTH
                ,decode_responses= True
                )

# Insert key values in redis
a1 = r.set( name = 'fly', value= 'eagle' )
r.set( name = 'bite', value= 'dog' )
r.set( name = 'claw', value= 'lion' )

value = r.get( name = 'fly' )
print( type( value ) )

if type( value ) == bytes:
    print( value.decode( 'utf-8' ) )    
else:
    print( value )

print( a1 )

