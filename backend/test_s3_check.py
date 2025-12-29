import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
django.setup()

from django.conf import settings
from core.models import HousePlan

print("=" * 60)
print("S3 UPLOAD TEST")
print("=" * 60)

print(f"\n1. Checking S3 Configuration:")
print(f"   USE_S3: {os.getenv('USE_S3')}")
print(f"   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"   MEDIA_URL: {settings.MEDIA_URL}")

# Check existing plans
print(f"\n2. Checking existing house plans:")
plans = HousePlan.objects.all()
print(f"   Total plans: {plans.count()}")

for plan in plans[:2]:
    print(f"\n   Plan: {plan.name}")
    if plan.image:
        print(f"   Image URL: {plan.image.url}")
        if 's3' in plan.image.url or 'amazonaws' in plan.image.url:
            print(f"   Status: OK - Image is in S3")
        else:
            print(f"   Status: WARNING - Image is local, not in S3")
    else:
        print(f"   Image: None")

print(f"\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
