'''
Description: Take as input a json, that has an array of dictionaries.
             Each dictionary represent a Card charge transaction.
             As output, this scrpt print the Status of each Transaction.
'''

import json 

def get_charge_completed( transactions ):
    # this method search if there is one transaction completed in an array of Card transactions.
    # parameters:
    #   transactions    Array of dictionaries. Each dictionary represent a Card charge transaction.

    try:
        #
        completed_tr = None

        for d in transactions:
            if d[ 'transaction_type' ] == 'charge' and d[ 'status' ].lower() == 'completed':
                completed_tr = d
                break

        return completed_tr
    except Exception as e:
        print( 'is_completed(), error: {}'.format( e ) )


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

    t = get_charge_completed( transactions )
    if t != None:
        print( '\n completed charge: \n' )
        print( json.dumps( t, indent = 3 ) )


print( '\n end. \n' )    
