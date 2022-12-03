'''
Description: Take as input a json, that has an array of dictionaries.
             Each dictionary represent a Card charge transaction.
             As output, the newest latest Transaction.
'''
from datetime import datetime
import json 

def find_completed_pending_newest( transactions ):
    # find the newset transaction completed in an array of Card transactions.
    # parameters:
    #   transactions    Array of dictionaries. Each dictionary represent a Card charge transaction.

    try:
        pending = None
        newest  = None

        for d in transactions:

            if d[ 'status' ].lower() == 'completed':
                return d
            elif d[ 'status' ].lower() == 'charge_pending':
                pending = d

            if newest == None:
                newest = d
                newest_dt =  datetime.fromisoformat( newest[ 'operation_date' ] )
                continue
            
            dt        = datetime.fromisoformat( d[ 'operation_date' ] )
            if newest_dt    < dt:
                newest      = d
                newest_dt   = dt

        if pending == None:
            return newest
        else:
            return pending

        
    except Exception as e:
        print( 'is_completed(), error: {}'.format( e ) )




file_path = '/home/art/data/op/x71.json'


with open( file_path, 'r') as f:
    
    # array of transactions
    transactions = json.load( f ) 

    print( '\nid\t\t\ttransaction_type\tstatus' )
    print( '\n-------------------- ------- --------\t\t------------' )


    for d in transactions:

        #print( 'd {}: \n'.format( json.dumps( d, indent = 3) ) )
        #print( d['id'], '\t', d['transaction_type'], '\t' , d['status'], d['operation_date'] )
        print( '{id} {transaction_type} {status}\t {operation_date}'.format( **d ) )

    t = find_completed_pending_newest( transactions )
    if t != None:
        print( '\n completed charge: \n' )
        print( json.dumps( t, indent = 3 ) )


print( '\n end. \n' )    
