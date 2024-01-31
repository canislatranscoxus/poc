'''
------------------------------------------------------------------------------
Description: Take as input a string that represent a python script,
             remove line breaks,
             and return as output the comments from the python script.
------------------------------------------------------------------------------
'''

import re

text = """
@My cool comments.
we like cats
and dogs.
@

# my code starts below
print( 'Hello world' )
"""

text = text.replace( '\n', ' ' )

str_pattern =  "@.+@"
pattern = re.compile( str_pattern )

result_match = pattern.match( text )
result_search = pattern.search( text )

if result_match != None:
    print( '\n result_match: ' )
    print( result_match.group( 0 ) )

if result_search != None:
    print( '\n result_search: ' )
    print( result_search.group( 0 ) )

