'''
-------------------------------------------------------------------------------
name       : Autocomplete Address Book. Redis example.

description: We will have a contact list with autocomplete feature included.
             this code use redis as memory cache for an auto complete.
                

             here we do 3 operations:



test:
    you can open redis client 
    (give pasword if needed. See your redis.conf requirepass)

    redis-cli -a my-super-long-password


    and see all the keys inserted with the next command

    ZRANGE members:wild 0 -1 WITHSCORES
    ZRANGE members:wild 0 -1 WITHSCORES



references:
    Redis in Action.
    https://redislabs.com/ebook/part-2-core-concepts/chapter-6-application-components-in-redis/6-1-autocomplete/6-1-1-autocomplete-for-recent-contacts/

-------------------------------------------------------------------------------
'''

import bisect
import redis
import os
import sys
import uuid

# -----------------------------------------------------------------------------
# attibutes
# -----------------------------------------------------------------------------

REDIS_HOST = os.environ[ 'REDIS_HOST' ]
REDIS_PORT = os.environ[ 'REDIS_PORT' ]
REDIS_DB   = 3
REDIS_AUTH = os.environ[ 'REDIS_AUTH' ]


conn = redis.Redis(  host     = REDIS_HOST
                    ,port     = REDIS_PORT
                    ,db       = REDIS_DB
                    ,password = REDIS_AUTH 
                    )

valid_characters = '`abcdefghijklmnopqrstuvwxyz{'
guild            = 'wild'
zset_name        = 'members:' + guild

# -----------------------------------------------------------------------------
# functions
# -----------------------------------------------------------------------------


def find_prefix_range( prefix ):
    posn    = bisect.bisect_left( valid_characters, prefix[-1:] )
    suffix  = valid_characters[ (posn or 1) - 1 ]
    return prefix[:-1] + suffix + '{', prefix + '{'


def autocomplete_on_prefix( conn, zset_name, prefix ):
    try:
        #
        start, end   = find_prefix_range( prefix )
        identifier   = str( uuid.uuid4() )
        start       += identifier
        end         += identifier
        #zset_name    = 'members:' + guild
        conn.zadd( zset_name, { start : 0, end : 0 } )

        pipeline = conn.pipeline(True)
        while 1:
            try:
                pipeline.watch( zset_name )

                sindex = pipeline.zrank( zset_name, start )
                eindex = pipeline.zrank( zset_name, end )
                erange = min( sindex + 9, eindex - 2 )

                # Find the ranks of our end points.
                pipeline.multi()
            except Exception as e:
                print( 'autocomplete_on_prefix(), pipeline, error: {}'.format( e ) )
                break

        print( '\n autocomplete \n\n' )
        # remove start end markers
        leave_guild( conn, guild, start )
        leave_guild( conn, guild, end   )

        matches = conn.zrange( zset_name, sindex, erange )
        a = []
        for i in matches:
            s = i.lower().decode("utf-8") 
            a.append( s )
        return a

    except Exception as e1:
        print( 'autocomplete_on_prefix(), error: {}'.format( e1 ) )
        raise





def join_guild( conn, guild, user ):
    conn.zadd( 'members:' + guild, { user : 0 } )
    
    


def leave_guild( conn, guild, user ):
    conn.zrem( 'members:' + guild, user )

# ----------------------------------------------------------------------------------

def prepare_test( conn, zset_name ):
    '''Insert animal names in sorted list in redis '''
    
    conn.delete( zset_name )
    
    file_path = "/home/art/git/poc/autocomplete/animals.txt"

    i = 0
    with open( file_path ) as file:
        line = file.readline()
        while line:
            

            user = line.strip()
            print( user )
            join_guild( conn, guild, user )

            line = file.readline()


def ut_01():
    print( 'find prefix range. ut 01' )

    prefix = 'abc'
    prefix_range = find_prefix_range( prefix )
    print( 'prefix_range: {}'.format( prefix_range ) )


def ut_02():
    print( 'Autocomplete Address Book. ut 02' )
    prefix = 'afr'
    a = autocomplete_on_prefix( conn, zset_name, prefix )
    print( 'prefix: {}'.format( prefix ) )
    for i in a:
        print( i )
    print( 'first: {}'.format( a[0] ) )
    print( 'last : {}'.format( a[ -1 ] ) )

def ut_03():
    print( 'Autocomplete Address Book. ut 03' )
    prefix = 'o'
    a = autocomplete_on_prefix( conn, zset_name, prefix )
    print( 'prefix: {}'.format( prefix ) )
    for i in a:
        print( i )
    print( 'first: {}'.format( a[0] ) )
    print( 'last : {}'.format( a[ -1 ] ) )



def ut_04():
    print( 'Autocomplete Address Book. ut 03' )
    prefix = 'c'
    a = autocomplete_on_prefix( conn, zset_name, prefix )
    print( 'prefix: {}'.format( prefix ) )
    for i in a:
        print( i )

    print( 'first: {}'.format( a[0] ) )
    print( 'last : {}'.format( a[ -1 ] ) )

if __name__ == "__main__":

    prepare_test( conn, zset_name )
    ut_02()
    ut_03()
    ut_04()
    print( '\n\n end.' )





