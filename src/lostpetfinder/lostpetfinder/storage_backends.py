"""
Custom storage backends definition
"""

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    """
    Media storage class using Amazon S3 storage to store upload file.
    """
    location = 'media'
    file_overwrite = False
