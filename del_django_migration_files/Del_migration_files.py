'''
description: this class delete migration files in a django project
'''

from os import path, remove
import glob


class Del_migration_files:

    base_dir = None
    apps = None

    def set_apps( self ):
        '''here we set which project we want clean from migration files.'''
        try:
            self.apps = None
            self.apps = [
                  'my_app_01'
                , 'my_app_02'
                , 'my_app_03'
            ]

            print( '\n apps: \n' )
            for i in self.apps:
                print( i )
            
        except Exception as e:
            print( 'Del_migration_files.set_apps(), error: {}'.format( e ) )

    def get_migration_files( self, project ):
        '''We get all the migration files from one project'''
        try:        
            a = []
            prj_dir = path.join( self.base_dir, project )

            my_paths = {
                '__pycache__'           : '*.pyc',
                'migrations'            : '[0-9][0-9][0-9][0-9]_*.py',
                'migrations/__pycache__': '*.pyc'
            }

            for dir, pattern in my_paths.items():
                my_path = path.join( prj_dir, dir, pattern )
                files   = glob.glob( my_path )
                a.extend( files )

            #print( '\n files in {}: \n'.format( project ) )
            #for i in a:
            #    print( i )

            return a

        except Exception as e:
            print( 'Del_migration_files.get_migration_files(), error: {}'.format( e ) )


    def delete_files( self, migration_files ):
        '''Here we delete all the migration files, usually from one project.'''
        print( '\n deleting... \n' )
        for f in migration_files:
            try:
                if path.exists( f ):
                    #print( f )
                    remove( f )
                else:
                    print( 'Not exists. {}'.format( f )  ) 
            except Exception as e:
                print( 'Del_migration_files.run(), error: {}'.format( e ) )
    

    def run( self ):
        try:
            
            for project in self.projects:
                files           = self.get_migration_files( project )
                self.delete_files( files )

        except Exception as e:
            print( 'Del_migration_files.run(), error: {}'.format( e ) )

    def __init__( self, base_dir ):
        self.base_dir = base_dir
        self.set_apps()

if __name__ == '__main__':
    base_dir = '/home/my_user/my_django/my_project/folder/'
    del_migration_files = Del_migration_files( base_dir = base_dir )
    del_migration_files.run()
    print( 'end. \n\n' )


