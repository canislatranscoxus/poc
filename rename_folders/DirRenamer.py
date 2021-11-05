'''
description: This script rename all the folders inside a path
'''
from genericpath import isdir
import os, sys
from os             import listdir
from os.path        import isfile, isdir
from os.path        import join


class DirRenamer:

    #dir_path = '/home/art/git/poc/rename_folders'


    def get_subfolders( self, dir_path ):
        print( '\n List folder: {}'.format( dir_path ) )

        for file_name in listdir( dir_path ):
            file_path = join( dir_path, file_name )
            if isdir( file_path ):
                print( file_path )


    def rename_subfolders( self, dir_path, delta ):
        '''This function rename all the folders inside a path. 
        The folders names are integers. for example:
            
            my_folder:
                1
                2
                3

        The new names will have a prefix "tmp_" and the integer number will increase summing delta.
        If delta = 10. So the result will be

            my_folder:
                tmp_10
                tmp_20
                tmp_30
        '''

        print( '\n Rename all subfolders inside: {}'.format( dir_path ) )
        for f in listdir( dir_path ):
            src = join( dir_path, f )
            if isdir( src ):
                try:
                    print( src )
                    n = str( int(f) + delta )
                    tar = join( dir_path, 'tmp_' + n )
                    os.rename( src, tar )
                except Exception as e:
                    print( 'error: {}'.format( e ) )


    def del_prefix_2_subfolders( self, dir_path, prefix = 'tmp_' ):
        '''This function rename all the folders inside a path. 
        Here we remove the prefix to the subfolders.For example:

        current folder

            my_folder:
                tmp_10
                tmp_20
                tmp_30

        The result will be
            my_folder:
                1
                2
                3
        '''

        print( '\n Rename all subfolders inside: {}'.format( dir_path ) )

        prefix_len = len( prefix )

        for f in listdir( dir_path ):
            src = join( dir_path, f )
            if isdir( src ):
                try:
                    print( src )
                    if f.startswith( prefix ):
                        new_file_name = f[ prefix_len : ]
                        tar = join( dir_path, new_file_name )
                        os.rename( src, tar )
                except Exception as e:
                    print( 'error: {}'.format( e ) )

