
class Transformer:

    def get_csv_row( self, clicoh_response, mysql_row ):
        try:
            d = {
                'id'                : mysql_row[ 'id' ], 
                'sku'               : mysql_row[ 'sku' ], 
                'clicoh_id'         : clicoh_response[ 'id' ], 
                'clicoh_variant_id' : clicoh_response[ 'variants' ][0][ 'id' ],
            }
            return d
        except Exception as e:
            print( 'Transformer.get_csv_row(), error: {}'.format( e ) )
            raise

