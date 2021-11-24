import redis
import os
import sys

REDIS_HOST = os.environ[ 'REDIS_HOST' ]
REDIS_PORT = os.environ[ 'REDIS_PORT' ]
#REDIS_DB   = os.environ[ 'REDIS_DB'   ]
REDIS_DB   = 10
REDIS_AUTH = os.environ[ 'REDIS_AUTH' ]


# connect to redis
r = redis.Redis( host     = REDIS_HOST
                ,port     = REDIS_PORT
                ,db       = REDIS_DB
                #,password = REDIS_AUTH
                ,decode_responses= True
                )

# Insert key values in redis
set_key = 'animals'
set_values = { 'falcon',  'coyote', 'hornet' }

r.delete( set_key )
r.sadd( set_key, *set_values  ) 

r.sadd( set_key, 'eagle' )
r.sadd( set_key, 'shark' )
r.sadd( set_key, 'tiger' )

animals_list = r.sscan( set_key, cursor=0 )[1]

for i in animals_list:
    print( i )

# ------------------------------------------------------------
# test Hash, dictionary.

r.hset( "boba", mapping={"age": 36, "name": "Boba Fett"} )
boba = r.hgetall("boba")
print( type( boba["name"] ), type(boba["age"]) )

# ------------------------------------------------------------


print( 'End' )

