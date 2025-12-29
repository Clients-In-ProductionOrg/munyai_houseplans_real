import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')

import django
django.setup()

from django.conf import settings
print(f"\n✓ DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"✓ MEDIA_URL: {settings.MEDIA_URL}")
print(f"✓ Ready for S3 uploads!\n")
