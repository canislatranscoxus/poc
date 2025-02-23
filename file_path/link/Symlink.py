'''
Create symbolic link for files in multiple folders
'''

import os, re, sys
from os             import listdir
from os.path        import isfile, isdir
from os.path        import join

class Symlink:

    # list of directories
    dirs = [
            '/home/art/tmp/a/',
            '/home/art/tmp/b/',
            '/home/art/tmp/c/',
    ]

    def create_symlinks(self, dir_path):
        try:
            file_pattern = re.compile( "_(\\d){6}.dat" )

            # get files
            for file_name in listdir(dir_path):
                file_path = join(dir_path, file_name)

                if isdir( file_path ):
                    continue

                if not file_name.endswith( '.dat' ):
                    continue

                # if it is this a renamed file, then skip it.
                result_search = file_pattern.search(file_name)
                if result_search != None:
                    continue

                date_sufix  = os.path.basename( dir_path )
                name, ext   = os.path.splitext( file_name )
                link_file   = '{}_{}.dat'.format( name, date_sufix )
                link_path   = os.path.join( dir_path, link_file )

                if os.path.isfile( link_path ):
                    continue

                print(link_path)
                os.symlink( file_path, link_path )

        except Exception as e:
            print('Symlink.create_symlinks(), error: {}'.format(e))
            raise


    def process_dir( self, dir_path ):
        # This method take as input one directory, get the date subdirectories,
        # and create the symlinks for its *.dat files.
        try:
            #print( 'process_dir(), ... begin' )
            #print( dir_path )

            str_pattern = "(\\d){6}"
            pattern = re.compile(str_pattern)

            # get subfolders
            for file_name in listdir(dir_path):
                file_path = join(dir_path, file_name)

                if isfile( file_path ):
                    continue

                result_search = pattern.search(file_name)
                if result_search == None:
                    continue

                #print( file_path )
                self.create_symlinks( file_path )

        except Exception as e:
            print('Symlink.process_dir(), error: {}'.format(e))
            raise

    def run(self):
        # create symlinks in all specified directories
        try:
            for d in self.dirs:
                self.process_dir( d )

        except Exception as e:
            print( 'Symlink.run(), error: {}'.format( e ) )
            raise

    def __ini__( self ):
        try:
            print( 'Symlink.__ini__() ... begin' )
        except Exception as e:
            print( 'Symlink.__ini__(), error: {}'.format( e ) )
