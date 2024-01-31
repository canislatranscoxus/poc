'''
------------------------------------------------------------------------------
Description: Take as input a string that represent a python script,
             remove line breaks,
             and return as output the comments from the python script.
------------------------------------------------------------------------------
'''

import re

text = """
'''My cool comments.
we like cats
and dogs.
'''

# my code starts below
print( 'Hello world' )
"""

print( '\n Our input text: ' )
print( text, '\n' )


text = text.replace( '\n', '' )

str_pattern =  "'''.+'''"
pattern = re.compile( str_pattern )

result = pattern.search( text )

if result == None:
    print( 'We did not find any match' )
else:
    print('Good news! we found: ')
    print( result.group( 0 ) )
