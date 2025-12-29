import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
django.setup()

from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from core.models import HousePlan

print("\n" + "=" * 70)
print("DJANGO ADMIN S3 UPLOAD TEST")
print("=" * 70)

print(f"\n1. Storage Configuration:")
print(f"   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"   MEDIA_URL: {settings.MEDIA_URL}")

from django.core.files.storage import default_storage
print(f"   Actual storage class: {default_storage.__class__.__name__}")

print(f"\n2. Creating test image...")
img = Image.new('RGB', (200, 200), color='green')
img_io = BytesIO()
img.save(img_io, 'PNG')
img_io.seek(0)

print(f"\n3. Creating HousePlan with image (same as Django admin would)...")
try:
    plan = HousePlan()
    plan.name = f"Admin Test {os.urandom(4).hex()}"
    plan.description = "Testing Django admin upload to S3"
    plan.price = 350000
    plan.square_feet = 2500
    plan.bedrooms = 4
    plan.bathrooms = 3
    plan.garage = 2
    
    # Save image the same way Django admin does
    plan.image.save('admin_test.png', ContentFile(img_io.getvalue()), save=False)
    
    # Save the plan
    plan.save()
    
    print(f"   ✓ Successfully saved!")
    print(f"   Plan ID: {plan.id}")
    print(f"   Image field: {plan.image}")
    print(f"   Image URL: {plan.image.url}")
    
    # Check if it's in S3
    if plan.image.url and ('s3' in plan.image.url or 'amazonaws' in plan.image.url):
        print(f"   ✓ SUCCESS - Image is in S3!")
    else:
        print(f"   ✗ ERROR - Image is NOT in S3!")
        print(f"   Image path: {plan.image.name if plan.image else 'None'}")
        
except Exception as e:
    print(f"   ✗ ERROR: {e}")
    import traceback
    traceback.print_exc()

print(f"\n" + "=" * 70)
