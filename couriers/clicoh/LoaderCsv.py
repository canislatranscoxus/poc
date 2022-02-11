import csv

class LoaderCsv:

    # csv header
    fieldnames  = [ 'id', 'name', 'sku', 'clicoh_id', 'clicoh_variant_id' ]

    f           = None # TextIOWrapper 
    writer      = None

    def write_rows( self, list_of_rows ):
        '''write multiple rows to csv file.
        list_of_rows: an list of dictionaries
        '''
        try:
            self.writer.writerows( list_of_rows )    
        except Exception as e:
            print( 'LoaderCsv.write_rows(), error: {}'.format( e ) )


    def create_file( self ):
        try:
            self.f = open('/home/art/data/clicoh_products.csv', 'w')
            self.writer = csv.DictWriter( self.f, fieldnames = self.fieldnames )
            self.writer.writeheader()
        except Exception as e:
            print( 'LoaderCsv.create_file(), error: {}'.format( e ) )


    def __init__(self) -> None:
        try:
            self.create_file()

        except Exception as e:
            print( 'LoaderCsv.__init__(), error: {}'.format( e ) )

    def __del__(self):
        # body of destructor
        try:
            self.f.close()
        except Exception as e:
            print( 'LoaderCsv.__init__(), error: {}'.format( e ) )


