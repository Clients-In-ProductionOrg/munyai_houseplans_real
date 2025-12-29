"""
S3 Storage backend that correctly handles Django's storage configuration
"""
from django.conf import settings


def get_storage():
    """Get the configured storage backend"""
    if settings.DEFAULT_FILE_STORAGE == 'storages.backends.s3boto3.S3Boto3Storage':
        from storages.backends.s3boto3 import S3Boto3Storage
        return S3Boto3Storage()
    else:
        from django.core.files.storage import FileSystemStorage
        return FileSystemStorage()
