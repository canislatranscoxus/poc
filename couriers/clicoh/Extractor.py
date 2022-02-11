import pymysql.cursors
import os

MYSQL_NAME     = os.environ[ 'MYSQL_NAME'     ]
MYSQL_USER     = os.environ[ 'MYSQL_USER'     ]
MYSQL_PASSWORD = os.environ[ 'MYSQL_PASSWORD' ]
MYSQL_HOST     = os.environ[ 'MYSQL_HOST'     ]


class Extractor:

    conn = None
    
    # en, es
    language_code = None

    # product id range. None range means, bring all the products.
    start_id = None
    end_id   = None 

    sql_base = """  
        SELECT  p.id as id,
                p.sku,
                t.name,
                t.description,
                p.width  as width,
                p.height as height,  
                p.length as length,
                p.weight
        FROM    shop_product              p join 
                shop_product_translation  t on  p.id = t.master_id 
        WHERE   t.language_code = 'es'  
            AND p.sku IS NOT NULL
        ORDER BY p.id """

    cursor = None

    def connect( self ):
        # Connect to the database
        self.conn = pymysql.connect(host        = MYSQL_HOST,
                                    user        = MYSQL_USER,
                                    password    = MYSQL_PASSWORD,
                                    database    = MYSQL_NAME,
                                    charset     = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor )


    def execute( self ):
        '''Select the rows execute a query of the style 
        
        SELECT fields 
        FROM   table
        WHERE  language = ...         '''
        try:
            self.cursor     = self.conn.cursor()
            number_of_rows  = self.cursor.execute( self.sql_base )

            print( 'query: \n\n {} \n\n'.format( self.sql_base ) )
            print( 'sql execute, number of rows: {}'.format( number_of_rows ) )

        except Exception as e:
            print( 'Extractor.execute(), error: {}'.format( e ) )
            raise


    def get_next_row( self ):
        pass

    def get_next_batch( self, num_of_rows = 20 ):
        '''
        get the next batch of rows using the
        :param int num_of_rows: The number of rows per batch
        '''
        try:
            rows = self.cursor.fetchmany( num_of_rows )
            return rows
            
        except Exception as e:
            print( 'Extractor.get_many(), error: {}'.format( e ) )
            self.conn.close()

    def close( self ):
        try:
            self.conn.close()
        except Exception as e:
            print( 'Extractor.close(), error: {}'.format( e ) )

    def __init__( self  ):
        try: 
            print( 'Extractor.__init__()...' )

        except Exception as e:
            print( 'Extractor.__init__(), error: {}'.format( e ) )
            print( self.sql_base )
            raise