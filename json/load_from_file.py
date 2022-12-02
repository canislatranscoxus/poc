import json 

file_path = '/home/art/data/op/71.json'


with open( file_path, 'r') as f:
    
    # array of transactions
    transactions = json.load( f ) 

    for d in transactions:
        print( 'd {}: \n'.format( json.dumps( d, indent = 3) ) )

print( '\n end. \n' )    
