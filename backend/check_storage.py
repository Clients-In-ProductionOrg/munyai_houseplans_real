import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
django.setup()

from django.conf import settings

print("\n" + "=" * 70)
print("DJANGO STORAGE CONFIGURATION CHECK")
print("=" * 70)

print(f"\n1. Environment Variables:")
print(f"   USE_S3 env var: {os.getenv('USE_S3')}")
print(f"   AWS_STORAGE_BUCKET_NAME: {os.getenv('AWS_STORAGE_BUCKET_NAME')}")
print(f"   AWS_S3_REGION_NAME: {os.getenv('AWS_S3_REGION_NAME')}")

print(f"\n2. Django Settings:")
print(f"   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"   MEDIA_URL: {settings.MEDIA_URL}")

if hasattr(settings, 'AWS_STORAGE_BUCKET_NAME'):
    print(f"   AWS_STORAGE_BUCKET_NAME: {settings.AWS_STORAGE_BUCKET_NAME}")
    print(f"   AWS_S3_REGION_NAME: {settings.AWS_S3_REGION_NAME}")
    print(f"   AWS_S3_CUSTOM_DOMAIN: {settings.AWS_S3_CUSTOM_DOMAIN}")
else:
    print(f"   AWS settings NOT found in Django settings!")

print(f"\n3. Storage Backend Test:")
from django.core.files.storage import default_storage

print(f"   default_storage class: {default_storage.__class__.__name__}")
print(f"   default_storage location: {default_storage.__class__.__module__}")

print(f"\n" + "=" * 70)
