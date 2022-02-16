import json

file_path = '/home/art/git/poc/skydropx/create_shipment_response.json'

f = open( file_path )
 
# returns JSON object as
# a dictionary
j = json.load(f)
f.close()



def format_fast_menu_rates( j ):
    # we loop the json j, the attribute 'included' is an array of dictionaries.
    data = {}
    try:
        for d in j[ 'included' ]:
            if d[ 'type' ] != 'rates':
                continue

            desc = '{service_level_name} {days} dias {total_pricing}'.format( **d[ 'attributes' ] )
            menu_rate = {
                'desc'          : desc,
                'service'       : d[ 'attributes' ][ 'service_level_name' ],
                'price'         : d[ 'attributes' ][ 'total_pricing'      ],
                'courier'       : d[ 'attributes' ][ 'provider'           ],
                'arriving_time' : d[ 'attributes' ][ 'days'               ],
                'courier_class' : 'CourierSkydropx'
            }
            data[ d['id'] ] = menu_rate
        return data
    except Exception as e:
        print( '.format_fast_menu_rates(), error: {}'.format( e ) )



data = format_fast_menu_rates( j )

print( '\n Menu Rates \n' )
print( json.dumps( data, indent = 3 ) )

print( '\n ... end' )