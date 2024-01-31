'''

links:
https://docs.python.org/3/library/datetime.html

'''

import os

from datetime import datetime
dt = datetime.now()

s = dt.isoformat()
print( '\n string in iso format : {}'.format( s ) )


# my custom format
s2 = dt.strftime('%Y-%m-%d-%H:%M:%S' )
#s2 = datetime.now().strftime('%Y%m%d-%H%M%S')
print ( 's2: {}'.format( s2 ) )


s3 = os.sep


print( '\n ... end.' )
