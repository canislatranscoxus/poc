import json
import requests

r = requests.post('https://httpbin.org/post', data = {'key':'value'})
j = r.json()

print( '\n\n my response: \n\n' )
print( json.dumps( j, indent = 3 ) )
print( '... end' )