import os
import django
from io import BytesIO
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
django.setup()

from django.conf import settings
from django.core.files.base import ContentFile
from core.models import HousePlan, HousePlanImage

print("\n" + "=" * 80)
print("SIMULATING DJANGO ADMIN IMAGE UPLOAD")
print("=" * 80)

print(f"\n1. STORAGE CONFIGURATION:")
print(f"   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"   MEDIA_URL: {settings.MEDIA_URL}")

# Create a test image (simulating file upload from admin)
print(f"\n2. CREATING TEST IMAGE:")
img = Image.new('RGB', (400, 300), color=(100, 150, 200))
img_io = BytesIO()
img.save(img_io, 'PNG')
img_io.seek(0)
print(f"   ✓ Created 400x300 test image")

# Create HousePlan (main image)
print(f"\n3. UPLOADING MAIN PLAN IMAGE (like clicking 'Add' in admin):")
try:
    plan = HousePlan.objects.create(
        name='S3 Test Plan - Admin Upload',
        description='Testing S3 upload through Django admin',
        price=499.99,
        bedrooms=4,
        bathrooms=3,
        garage=2,
        square_feet=3500
    )
    
    # Save the image
    plan.image.save(
        'admin_test_image.png',
        ContentFile(img_io.getvalue()),
        save=True
    )
    
    print(f"   ✓ Plan created: {plan.name}")
    print(f"   ✓ Image file: {plan.image.name}")
    print(f"   ✓ Image URL: {plan.image.url}")
    
    # Check storage type
    storage_class = plan.image.storage.__class__.__name__
    print(f"   ✓ Storage: {storage_class}")
    print(f"   ✓ In S3: {'Yes ✓' if 'amazonaws' in plan.image.url else 'No ✗'}")
    
except Exception as e:
    print(f"   ✗ ERROR: {e}")
    import traceback
    traceback.print_exc()

# Add gallery image
print(f"\n4. UPLOADING GALLERY IMAGE (like adding to gallery in admin):")
try:
    gallery_img = HousePlanImage.objects.create(
        house_plan=plan,
        title='Front View',
        order=1
    )
    
    # Save image
    img_io.seek(0)
    gallery_img.image.save(
        'admin_gallery_test.png',
        ContentFile(img_io.getvalue()),
        save=True
    )
    
    print(f"   ✓ Gallery image created: {gallery_img.title}")
    print(f"   ✓ Image file: {gallery_img.image.name}")
    print(f"   ✓ Image URL: {gallery_img.image.url}")
    print(f"   ✓ Storage: {gallery_img.image.storage.__class__.__name__}")
    print(f"   ✓ In S3: {'Yes ✓' if 'amazonaws' in gallery_img.image.url else 'No ✗'}")
    
except Exception as e:
    print(f"   ✗ ERROR: {e}")
    import traceback
    traceback.print_exc()

print(f"\n" + "=" * 80)
print("TEST COMPLETE - Check S3 bucket for uploaded images!")
print("=" * 80 + "\n")
