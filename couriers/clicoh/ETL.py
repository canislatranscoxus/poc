'''
description: This ETL move data from MySQL to ClicoH.
                We Extract products data from MySQL, 
                Transform, and Load to ClicoH.

                At the end we save a csv file with product_id, clicoh_id, clicoh_variant_id.
'''

from Extractor      import Extractor
from Transformer   import Transformer
from LoaderCsv      import LoaderCsv
from CourierClicoh  import CourierClicoh
#from Params import Params


class ETL:

    # attributes
    #params = None
    #loader = None

    # ------------------------------------------------------------------------------
    # methods 
    # ------------------------------------------------------------------------------

    def clean_previous_etl( self ):
        if self.params.loader[ 'is_kill_n_fill' ] == True:
            self.loader.clean_previous_etl( )

    def persist( self, ):
        pass

    def process_all( self ):
        '''This method Extract all the rows SELECTed from the table (mySQL product_translation),
        Transform, and  Load to Redis. This is used for Kill and Fill'''

        try:
            extractor   = Extractor  ( )
            #transformer= Transformer( self.params )
            extractor.connect()
            num_of_rows = 20
            extractor.execute()
            rows        = extractor.get_next_batch( num_of_rows )
            transformer = Transformer()
            courier     = CourierClicoh()
            loader      = LoaderCsv()

            while len( rows ) > 0:
                products = []
                for row in rows:
                    print( 'id : {}'.format( row[ 'id' ] ) )
                    j = courier.add_product( row )

                    product  = transformer.get_csv_row( j, row )
                    '''d = {
                         'id'                   : row[ 'id'                 ], 
                         'sku'                  : row[ 'sku'                ], 
                         'clicoh_id'            : "row[ 'clicoh_id'          ]", 
                         'clicoh_variant_id'    : "row[ 'clicoh_variant_id'  ]",
                    }'''
                    products.append( product )
                    
                loader.write_rows( products )
                rows = extractor.get_next_batch( num_of_rows )

            extractor.close()
            print( '\n ETL.procell_all() ... end' )

        except Exception as e:
            print( 'ETL.process_all(), error: {}'.format( e ) )
            raise

    def run( self ):
        try:
            #if self.params.loader[ 'is_kill_n_fill' ]:
            #    self.clean_previous_etl()

            self.process_all()
            #self.loader.ut_search()

        except Exception as e:
            print( 'ETL.run(), error: {}'.format( e ) )
            raise
        

    def __init__( self, params = None ):
        try:
            print( 'ETL.__init__()' )
            #self.params = params
            #self.loader   = Loader_dao_redis( params )
        except Exception as e:
            print( 'ETL.__init__(), error: {}'.format( e ) )
            raise
