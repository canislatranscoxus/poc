'''
Description: Example of loading a config file


references: https://docs.python.org/3/library/configparser.html
'''
import configparser

config = configparser.ConfigParser()
file_path = '/home/art/git/poc/load_config/config.ini'
config.read( file_path )

print( config.sections() )
# ['bitbucket.org', 'topsecret.server.com']

print(  'bitbucket.org' in config )
#True

print( 'bytebong.com' in config )
#False

#print( config[ 'non_exist_section' ][ 'non_exist_param' ] )


print( config['bitbucket.org']['User'] )
#'hg'

print( config['DEFAULT']['Compression'] )
# yes

'''def my_convert ( v, t):
    print( v )
    print( type( v ) )
    x = t( v )
    print( x )
    print( type( x ) )

a= 'True'
x = my_convert( a, bool )



'''