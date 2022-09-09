''' 
This script makes an INSERT_INTO_table  SQL query
'''

def get_query( fields_array ):
    try:
        field_names = ','.join( fields_array )
        field_values = ''
        for i in a:
            if field_values == '':
                field_values = '%({})s'.format( i )
            else:
                field_values = field_values + ',%({})s'.format( i )

        sql = '''INSERT INTO my_table 
        ( {field_names} ) 
        values 
        ( {field_values} ) '''.format( 
            field_names = field_names, 
            field_values = field_values )

        return sql
    except Exception as e:
        print( 'error: {}'.format( e ) )




a   = [ 'field_1', 'field_2', 'field_3'  ]
sql = get_query( a )
print( '\n sql: {} \n'.format( sql ) )




