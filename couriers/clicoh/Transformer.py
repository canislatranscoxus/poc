
class Transformer:

    def get_csv_row( self, clicoh_j, mysql_row ):
        try:
            d = {
                'id'                : mysql_row[ 'id'   ], 
                'name'              : mysql_row[ 'name' ],                 
                'sku'               : mysql_row[ 'sku'  ], 
                'clicoh_id'         : clicoh_j [ 'id'   ], 
                'clicoh_variant_id' : clicoh_j [ 'variants' ][0][ 'id' ],
            }
            return d
        except Exception as e:
            print( 'Transformer.get_csv_row(), error: {}'.format( e ) )
            raise

