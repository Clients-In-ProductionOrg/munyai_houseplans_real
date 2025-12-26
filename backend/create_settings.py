#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')
django.setup()

from core.models import SiteSettings

# Delete existing if any
SiteSettings.objects.all().delete()

# Create default settings with proper embed URL
settings = SiteSettings.objects.create(
    youtube_link='https://www.youtube.com/embed/ciXvD_-rtts?si=vgL--Q5gRYliXpUZ&autoplay=1&mute=1&loop=1&playlist=ciXvD_-rtts',
    company_phone='+27 123 456 789',
    company_email='info@cedric.co.za',
    company_address='123 Main Street, Johannesburg, South Africa'
)
print(f'✓ SiteSettings created successfully!')
print(f'✓ YouTube Link: {settings.youtube_link}')
