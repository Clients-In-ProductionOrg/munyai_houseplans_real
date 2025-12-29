#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
sys.path.insert(0, os.path.dirname(__file__))

django.setup()

from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from core.models import HousePlan

print('\n' + '=' * 70)
print('S3 UPLOAD TEST')
print('=' * 70)

print(f'\n1. Configuration:')
print(f'   USE_S3: {os.getenv("USE_S3")}')
print(f'   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}')
print(f'   AWS_BUCKET: {os.getenv("AWS_STORAGE_BUCKET_NAME")}')
print(f'   AWS_REGION: {os.getenv("AWS_S3_REGION_NAME")}')

# Create test image
print(f'\n2. Creating test image...')
img = Image.new('RGB', (100, 100), color='blue')
img_io = BytesIO()
img.save(img_io, 'PNG')
img_io.seek(0)

# Create house plan and upload
print(f'\n3. Uploading to S3...')
try:
    plan = HousePlan.objects.create(
        name=f'Test Upload {os.urandom(4).hex()}',
        description='Testing S3 upload',
        price=299.99,
        bedrooms=3,
        bathrooms=2,
        square_feet=2000
    )
    plan.image.save('test.png', ContentFile(img_io.getvalue()), save=True)
    
    print(f'   ✓ Successfully uploaded')
    print(f'   Image URL: {plan.image.url}')
    
    if 'amazonaws' in plan.image.url:
        print(f'   ✓ Confirmed in S3!')
    else:
        print(f'   ✗ NOT in S3 - URL is: {plan.image.url}')
        
except Exception as e:
    print(f'   ✗ ERROR: {e}')
    import traceback
    traceback.print_exc()

print('\n' + '=' * 70)
