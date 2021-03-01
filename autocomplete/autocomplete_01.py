'''
name       : Autocomplete for contact list. Redis example.

description: We will have a contact list with autocomplete feature included.
             this code use redis as memory cache for an auto complete.
                

             here we do 3 operations:

    🔥 Remove the contact from the list if it exists.
    🔥 Add the contact to the beginning of the list.
    🔥 Trim the list if it now has more than 100 items.


test:
    you can open redis client 
    (give pasword if needed. See your redis.conf requirepass)

    redis-cli -a my-super-long-password


    and see all the keys inserted with the next command

    lrange "recent:ryu" 0 -1


references:
    Redis in Action.
    https://redislabs.com/ebook/part-2-core-concepts/chapter-6-application-components-in-redis/6-1-autocomplete/6-1-1-autocomplete-for-recent-contacts/

'''

import redis
import os
import sys

REDIS_HOST = os.environ[ 'REDIS_HOST' ]
REDIS_PORT = os.environ[ 'REDIS_PORT' ]
REDIS_DB   = 2
REDIS_AUTH = os.environ[ 'REDIS_AUTH' ]


print( 'shop.recommender.py ... connecting to redis' ) 
conn = redis.Redis(  host     = REDIS_HOST
                    ,port     = REDIS_PORT
                    ,db       = REDIS_DB
                    ,password = REDIS_AUTH 
                    )
print( 'shop.recommender.py ... connection OK' ) 



def add_update_contact(conn, user, contact):
    ac_list = 'recent:' + user
    pipeline = conn.pipeline(True)
    count = 1
    pipeline.lrem( ac_list, count, contact )  

    pipeline.lpush(ac_list, contact)
    pipeline.ltrim(ac_list, 0, 99)
    pipeline.execute()

def remove_contact(conn, user, contact):
    count = 1
    conn.lrem('recent:' + user, count,contact)




def fetch_autocomplete_list(conn, user, prefix):
    candidates = conn.lrange('recent:' + user, 0, -1)
    matches = []
    for candidate in candidates:
        s = candidate.lower().decode("utf-8") 
        if s.startswith(prefix):
            matches.append( s )
    
    return matches


def ut_01():
    user = 'ryu'
    contact = 'chun li'
    add_update_contact( conn, user, contact )

    contact = 'bison'
    add_update_contact( conn, user, contact )

    contact = 'cardi b'
    add_update_contact( conn, user, contact )

    contact = 'cammy'
    add_update_contact( conn, user, contact )

    contact = 'ken'
    add_update_contact( conn, user, contact )

    contact = 'kelly'
    add_update_contact( conn, user, contact )

    contact = 'kussy'
    add_update_contact( conn, user, contact )

    contact = 'bison'
    remove_contact( conn, user, contact )

    matches = fetch_autocomplete_list( conn, user, 'c' )

    print( '\n Autocomplete for c \n' )
    for i in sorted( matches ):
        print( 'i: {}'.format( i ) )

    matches = fetch_autocomplete_list( conn, user, 'k' )
    print( '\n Autocomplete for k \n' )
    for i in sorted( matches ) :
        print( 'i: {}'.format( i ) )


if __name__ == "__main__":
    ut_01()
    print( '\n\n end.' )

