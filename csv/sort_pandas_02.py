'''
description: this script uses pandas to 

            * create a dataframe from an array of dictionaries,
            * SELECT some columns
            * ORDER BY a column in ASC or DESC
            * print sorted data to console

'''

import pandas as pd
import json

file_path = '/home/art/git/poc/csv/data.json'

f = open( file_path )
# returns JSON object as
# a dictionary
my_dic = json.load(f)
f.close()

print( 'original data' )
print( json.dumps( my_dic, indent = 3 ) )

df_original = pd.DataFrame( my_dic )
df = df_original.get( [ 'price', 'arriving_time', 'service', 'courier' ] )
#df = df_original.eval .eval( 'price = float( price )' )


print( '\n Sorted by price, cheapest goes first' )
df_by_price_asc = df.sort_values( by= 'price', ascending= True )
print( df_by_price_asc.to_string() )

print( '\n select first row, and two columns by name' )
row =  df_by_price_asc[ ['price' , 'courier'] ].iloc[ 0 ]
print( row )


print( '\n sorted by price, most expensive goes first' )
df_by_price_desc = df.sort_values( by= 'price', ascending= False )
print( df_by_price_desc.to_string() )

print( '\n sorted by arriving_time, from fastest goes first' )
df_by_atime_asc = df.sort_values( by= 'arriving_time', ascending= True )
print( df_by_atime_asc.to_string() )

print( '\n sorted by arriving_time, from slowest goes first' )
df_by_atime_desc = df.sort_values( by= 'arriving_time', ascending= False )
print( df_by_atime_desc.to_string() )

#print( df.to_string() )


print( '\n ... end' )