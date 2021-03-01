'''
write a txt file in gcp Cloud Storage 

pip install GoogleAppEngineCloudStorageClient

#pip install google-cloud-storage
#pip install cloudstorage
'''

import os
import cloudstorage as gcs

filename = 'gs://aat_bk/p1.log'

#[START retries]
my_default_retry_params = gcs.RetryParams(initial_delay=0.2,
                                          max_delay=5.0,
                                          backoff_factor=2,
                                          max_retry_period=15)

gcs.set_default_retry_params(my_default_retry_params)
write_retry_params = gcs.RetryParams(backoff_factor=1.1)

gcs_file = gcs.open(filename,
    'w',
    content_type='text/plain',
    options={'x-goog-meta-foo': 'foo',
            'x-goog-meta-bar': 'bar'},
    retry_params=write_retry_params)

gcs_file = cloudstorage.open(
    filename, 
    'w', 
    content_type='text/plain', 
    options={'x-goog-acl': 'private','x-goog-meta-foo': 'foo', 'x-goog-meta-bar': 'bar'}
    )


gcs_file.write( 'hello \n')
gcs_file.write( 'my friends \n')
gcs_file.close()

