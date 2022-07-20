import json

params = { 
    'order_id' : 7,
    'doc_type' : 'invoice'
 }

task_name = '{order_id}_{doc_type}'.format( **params )

print( task_name )