'''

'''

import argparse
#from Params import Params
from ETL import ETL



def get_args():
    parser = argparse.ArgumentParser( 
        prog        = 'main',
        description = '''This script run the ETL process from mySQL to Redis, for Full Text Search.''',
        epilog      = '''Set your params in a config file!
                    '''
        )

    parser.add_argument( '-c', '--config'  , type = str , default = './config.ini'  , help = 'path of config file')
    args = parser.parse_args()
    return args

def main( ):
    try:
        #params = Params( args.config )
        etl = ETL( )
        etl.run()

        #etl.clean_previous_etl()    
    except Exception as e:
        print( 'main(), error: {}'.format( e ) )
    

if __name__ == '__main__':
    #args = get_args()
    #main( args )    
    #args.config ='/home/art/git/basmati_gcp/etl_tfidf/config/dev.ini'
    #print( '\n args.config: {} \n'.format( args.config ) )
    
    main( )
    print( '\n main ... end. \n' )