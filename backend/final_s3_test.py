import os
import django
from io import BytesIO
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
django.setup()

from django.conf import settings
from django.core.files.base import ContentFile
from core.models import HousePlan

print("\n" + "=" * 70)
print("TESTING S3 UPLOAD VIA DJANGO")
print("=" * 70)

print(f"\nStorage Config:")
print(f"  DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"  MEDIA_URL: {settings.MEDIA_URL}")

# Create test image
print(f"\nCreating test image...")
img = Image.new('RGB', (200, 200), color='red')
img_io = BytesIO()
img.save(img_io, 'PNG')
img_io.seek(0)

# Create house plan with image
print(f"Creating HousePlan with S3 upload...")
try:
    plan = HousePlan.objects.create(
        name=f'S3Test_{os.urandom(3).hex()}',
        description='Testing S3 upload',
        price=299.99,
        bedrooms=3,
        bathrooms=2,
        square_feet=2000
    )
    
    plan.image.save(
        f'test_{os.urandom(3).hex()}.png',
        ContentFile(img_io.getvalue()),
        save=True
    )
    
    print(f"\n✓ SUCCESS!")
    print(f"  Plan: {plan.name}")
    print(f"  Image URL: {plan.image.url}")
    print(f"  In S3: {'amazonaws' in plan.image.url}")
    
except Exception as e:
    print(f"\n✗ FAILED: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
