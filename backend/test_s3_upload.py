#!/usr/bin/env python
"""
Test script to verify S3 upload functionality
Run this with: python manage.py shell < test_s3_upload.py
"""
import os
import django
from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
django.setup()

from core.models import HousePlan

print("=" * 60)
print("S3 UPLOAD TEST")
print("=" * 60)

# Check if S3 is enabled
print(f"\n1. Checking S3 Configuration:")
print(f"   USE_S3 env: {os.getenv('USE_S3')}")
print(f"   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"   MEDIA_URL: {settings.MEDIA_URL}")
print(f"   AWS_STORAGE_BUCKET_NAME: {settings.AWS_STORAGE_BUCKET_NAME if hasattr(settings, 'AWS_STORAGE_BUCKET_NAME') else 'Not set'}")

# Create a test image in memory
print(f"\n2. Creating test image...")
img = Image.new('RGB', (100, 100), color='red')
img_io = BytesIO()
img.save(img_io, 'PNG')
img_io.seek(0)

# Create a test house plan with image
print(f"\n3. Creating test HousePlan with S3 upload...")
try:
    test_plan = HousePlan(
        name='S3 Upload Test',
        description='Testing S3 upload functionality',
        price=299.99,
        bedrooms=3,
        bathrooms=2,
        garage=1,
        square_feet=2000,
    )
    
    # Save image to the model
    test_plan.image.save('test_s3_image.png', ContentFile(img_io.getvalue()))
    test_plan.save()
    
    print(f"   ✅ HousePlan created successfully!")
    print(f"   Plan ID: {test_plan.id}")
    print(f"   Plan Name: {test_plan.name}")
    
except Exception as e:
    print(f"   ❌ Error creating plan: {str(e)}")
    import traceback
    traceback.print_exc()

# Verify the image URL
print(f"\n4. Checking image URL...")
try:
    plan = HousePlan.objects.filter(name='S3 Upload Test').first()
    if plan and plan.image:
        image_url = plan.image.url
        print(f"   Image URL: {image_url}")
        
        if 's3' in image_url.lower() or 'amazonaws' in image_url.lower():
            print(f"   ✅ Image is in S3 (URL contains 's3' or 'amazonaws')")
        else:
            print(f"   ❌ Image is NOT in S3 (URL is local)")
    else:
        print(f"   ❌ Plan or image not found")
        
except Exception as e:
    print(f"   ❌ Error checking URL: {str(e)}")

print(f"\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
