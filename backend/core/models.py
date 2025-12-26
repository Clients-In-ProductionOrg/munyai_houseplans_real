"""
Core app models - Define your application models here
"""
from django.db import models
from django.contrib.auth.models import User


class SiteSettings(models.Model):
    """Model for site-wide configuration and settings"""
    youtube_link = models.URLField(blank=True, null=True, help_text="YouTube channel or video link (short or embed format)")
    company_phone = models.CharField(max_length=20, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    about_text = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Site Settings'

    def get_embed_youtube_url(self):
        """Convert any YouTube URL format to embed format"""
        if not self.youtube_link:
            return None
        
        url = self.youtube_link
        video_id = None
        
        # Extract video ID from different YouTube URL formats
        if 'youtu.be/' in url:
            # Short format: https://youtu.be/VIDEO_ID
            video_id = url.split('youtu.be/')[-1].split('?')[0]
        elif 'youtube.com/watch?v=' in url:
            # Watch format: https://www.youtube.com/watch?v=VIDEO_ID
            video_id = url.split('v=')[-1].split('&')[0]
        elif 'youtube.com/embed/' in url:
            # Already in embed format
            return url
        
        # Convert to embed format
        if video_id:
            return f'https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1'
        
        return url

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            self.pk = SiteSettings.objects.first().pk
        super().save(*args, **kwargs)

class HousePlan(models.Model):
    """Model for house plans"""
    DISPLAY_CHOICES = [
        ('house-plans', 'House Plans Page'),
        ('built-homes', 'Built Homes Page'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, default=1)
    garage = models.IntegerField(default=1)
    square_feet = models.IntegerField()
    width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Width in meters")
    depth = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Depth in meters")
    image = models.ImageField(upload_to='plans/', blank=True, null=True, help_text="Primary/thumbnail image")
    video_url = models.URLField(blank=True, null=True, help_text="YouTube video URL")
    display_on = models.CharField(max_length=20, choices=DISPLAY_CHOICES, default='house-plans', help_text="Choose where to display this house plan")
    is_popular = models.BooleanField(default=False, help_text="Show in 'Popular House Plans' section")
    is_best_selling = models.BooleanField(default=False, help_text="Show in 'Best-Selling Designs' section")
    is_new = models.BooleanField(default=False)
    pet_friendly = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'House Plan'
        verbose_name_plural = 'House Plans'


class HousePlanImage(models.Model):
    """Model for multiple images per house plan"""
    house_plan = models.ForeignKey(HousePlan, on_delete=models.CASCADE, related_name='plan_images')
    image = models.ImageField(upload_to='plans/')
    title = models.CharField(max_length=200, blank=True, null=True, help_text="Image title or description")
    order = models.IntegerField(default=0, help_text="Order to display images")
    
    def __str__(self):
        return f"{self.house_plan.name} - {self.title or 'Image'}"
    
    class Meta:
        ordering = ['order']
        verbose_name = 'House Plan Image'
        verbose_name_plural = 'House Plan Images'


class Floor(models.Model):
    """Model for individual floors in a house plan"""
    LEVEL_CHOICES = [
        ('ground', 'Ground Floor'),
        ('first', 'First Floor'),
        ('second', 'Second Floor'),
        ('third', 'Third Floor'),
        ('fourth', 'Fourth Floor'),
        ('fifth', 'Fifth Floor'),
        ('sixth', 'Sixth Floor'),
        ('seventh', 'Seventh Floor'),
        ('other', 'Other'),
    ]
    
    house_plan = models.ForeignKey(HousePlan, on_delete=models.CASCADE, related_name='floors')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='ground')
    floor_area = models.IntegerField()
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    lounges = models.IntegerField(default=0)
    dining_areas = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True, help_text="Floor-specific notes or description")
    order = models.IntegerField(default=0, help_text="Order to display floors")
    
    def __str__(self):
        return f"{self.house_plan.name} - {self.get_level_display()}"
    
    class Meta:
        ordering = ['order', 'level']
        verbose_name = 'Floor'
        verbose_name_plural = 'Floors'
        unique_together = ('house_plan', 'level')


class Feature(models.Model):
    """Model for house plan features"""
    house_plan = models.ForeignKey(HousePlan, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.house_plan.name} - {self.name}"
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


class Amenity(models.Model):
    """Model for house plan amenities"""
    house_plan = models.ForeignKey(HousePlan, on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.house_plan.name} - {self.name}"
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'


class BuiltHome(models.Model):
    """Model for built homes/projects"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=300)
    image = models.ImageField(upload_to='homes/', blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Built Home'
        verbose_name_plural = 'Built Homes'


class Contact(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200, default='General Inquiry')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'


class Quote(models.Model):
    """Model for quote requests"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    house_plan = models.ForeignKey(HousePlan, on_delete=models.SET_NULL, related_name='quotes', null=True, blank=True)
    requirements = models.TextField(blank=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.house_plan:
            return f"Quote from {self.name} for {self.house_plan.name}"
        return f"Quote from {self.name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Quote Request'
        verbose_name_plural = 'Quote Requests'


class Purchase(models.Model):
    """Model for tracking plan purchases and payments"""
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    
    # Customer Information
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pickup_point = models.CharField(max_length=200, blank=True, null=True)
    area_mall = models.CharField(max_length=200, blank=True, null=True)
    
    # Plan Information
    house_plan = models.ForeignKey(HousePlan, on_delete=models.SET_NULL, related_name='purchases', null=True, blank=True)
    plan_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Payment Information
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    yoco_payment_id = models.CharField(max_length=200, blank=True, null=True, help_text="Yoco payment transaction ID")
    yoco_reference = models.CharField(max_length=200, blank=True, null=True, help_text="Yoco reference number")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(blank=True, null=True, help_text="When payment was completed")
    
    def __str__(self):
        plan_name = self.house_plan.name if self.house_plan else 'N/A'
        return f"Purchase from {self.name} for {plan_name} - {self.payment_status}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
