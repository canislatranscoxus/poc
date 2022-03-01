'''
description: This class allow to upload and download objects from Cloud Storage.
                The objects can be files, or strings.

links:
    https://cloud.google.com/storage/docs/downloading-objects#downloading-an-object
'''
import json
from os.path    import join
from shutil     import copy

from GCS        import GCS

class DataLakeConnector:

    # this is the bucket on cloud
    bucket    = None

    # a switch for run on cloud or local
    on_cloud  = True

    # Directory in my local laptop, when Datalake is locally.
    local_dir = None

    def upload_from_string( self, src, tar ):
        '''read a string and upload as a file in data lake.
        src : is a string
        tar : the file path inside data lake/bucket. 
        '''
        try:

            if self.on_cloud:
                GCS.upload_blob_from_string( self.bucket, src, tar )
            else:
                file_path = join( self.local_dir, tar )
                with open( file_path , 'w') as f:
                    f.write( src )
        except Exception as e:
            print( 'DataLakeConnector.upload_from_string(), error: {}'.format( e ) )

    def upload_from_dict( self, src, tar ):
        '''read a Dictionary and upload as a file in data lake.
        src : is a Dictionary
        tar : the file path inside data lake/bucket. 
        '''
        try:
            if self.on_cloud:
                s = json.dumps( src )
                GCS.upload_blob_from_string( self.bucket, s, tar )
            else:
                file_path = join( self.local_dir, tar )
                with open( file_path , 'w') as f:
                    json.dump( src, f)
        except Exception as e:
            print( 'DataLakeConnector.upload_from_dict(), error: {}'.format( e ) )

    def upload_from_file( self, src, tar ):
        '''upload a file to data lake
        src : source file path 
        tar : target file path, in data lake. 
        '''
        try:
            if self.on_cloud:
                GCS.upload_blob( self.bucket, src, tar )
            else:
                file_path = join( self.local_dir, tar )
                copy( src, file_path )

        except Exception as e:
            print( 'DataLakeConnector.upload_from_file(), error: {}'.format( e ) )


    def download( self, src, tar ):
        '''read a file in data lake and download it to local machine.
        src : the file path inside data lake/bucket. 
        tar : file path in our local machine. Directories must exist.
        '''
        try:
            if self.on_cloud:
                GCS.download_blob( self.bucket, src, tar )
            else:
                file_path = join( self.local_dir, src )
                copy( file_path, tar )

        except Exception as e:
            print( 'DataLakeConnector.download(), error: {}'.format( e ) )


    def download_as_string( self, src ):
        '''read a file in data lake and download it to local machine.
        src : the file path inside data lake/bucket. 
        tar : file path in our local machine. Directories must exist.
        '''
        try:
            s = None
            if self.on_cloud:
                s = GCS.get_str_from_blob( self.bucket, src )
            else:
                file_path = join( self.local_dir, src )
                with open( file_path, 'r') as reader:
                    s = reader.read()
            return s

        except Exception as e:
            print( 'DataLakeConnector.download_as_string(), error: {}'.format( e ) )



    def __init__(self, params :dict = None) -> None:
        self.on_cloud  = params[ 'ON_CLOUD'     ]
        self.bucket    = params[ 'DL_BUCKET'    ]
        self.local_dir = params[ 'DL_LOCAL_DIR' ]
