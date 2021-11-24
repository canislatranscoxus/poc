'''
here we upload a text file to gcp google Cloud Storage 

dev samples
https://download.huihoo.com/google/gdgdevkit/DVD1/developers.google.com/storage/docs/gspythonlibrary.html

'''

from google.cloud import storage
import io

def upload_blob_from_string( bucket_name, src_string, tar_blob_name ):
    # Get the bucket that the file will be uploaded to.
    storage_client = storage.Client()
    bucket = storage_client.get_bucket( bucket_name )

    # Create a new blob and upload the file's content.
    my_file = bucket.blob( tar_blob_name )

    # create in memory file
    output = io.StringIO( src_string )

    # upload from string
    my_file.upload_from_string(output.read(), content_type="text/plain")

    output.close()

    # list created files
    blobs = storage_client.list_blobs(bucket)
    for blob in blobs:
        print(blob.name)

    # Make the blob publicly viewable.
    my_file.make_public()