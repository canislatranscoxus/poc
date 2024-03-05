'''
This script load a environment variable
'''

import os

REDIS_HOST = os.environ[ 'REDIS_HOST' ]

print( 'my environment variable REDIS_HOST: {}'.format( REDIS_HOST ) )


