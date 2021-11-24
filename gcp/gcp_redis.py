'''
This is a small test using redis in python.


on google gcp

sudo apt-get install telnet

telnet <your-redis-server> 6379


'''

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
                ,password = REDIS_AUTH
                ,decode_responses= True
                )

# Insert key values in redis
r.set( name = 'fly', value= 'eagle' )
r.set( name = 'bite', value= 'dog' )
r.set( name = 'claw', value= 'lion' )

# get all the key values from redis
keys = r.keys( '*' )
for key in keys:
    try:
        v = r.get( key )
        print( '{} : {}'.format( key, v )  )
    except Exception as e:
        print( 'error getting value of key: {}'.format( key ) )

print( '\n\n end.' )