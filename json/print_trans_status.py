'''
Description: Take as input a json, that has an array of dictionaries.
             Each dictionary represent a payment transaction.
             As output, this scrpt print the Status of each Transaction.
'''

import json 

file_path = '/home/art/data/op/71.json'


with open( file_path, 'r') as f:
    
    # array of transactions
    transactions = json.load( f ) 

    print( '\nid\t\t\ttransaction_type\tstatus' )
    print( '\n-------------------- ------- --------\t\t------------' )


    for d in transactions:

        #print( 'd {}: \n'.format( json.dumps( d, indent = 3) ) )
        #print( d['id'], '\t', d['transaction_type'], '\t' , d['status'], d['operation_date'] )
        print( '{id} {transaction_type} {status}\t {operation_date}'.format( **d ) )

print( '\n end. \n' )    
