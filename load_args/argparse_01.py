'''
description: this script shows how load command line arguments.

usage:

>  python argparse_01.py 


references: https://docs.python.org/3/library/argparse.html
'''
import argparse
parser = argparse.ArgumentParser( 
    prog        = 'argparse_01',
    description = '''this script take your pet data and print it on screen''',
    epilog      = '''register your pet now!
                  '''
    )

parser.add_argument( '-p', '--petname'  , type = str , default = 'X'  , help = 'name of your pet')
parser.add_argument( '-y', '--years'    , type = int , default = '1'  , help = 'age in years'  )
parser.add_argument( '-d', '--dangerous', type = bool, default = False, help = 'is dangerous'  )

args = parser.parse_args()

print( args )
print( 'petname  : {}'.format( args.petname ) )
print( 'years    : {}'.format( args.years ) )
print( 'dangerous: {}'.format( args.dangerous ) )
