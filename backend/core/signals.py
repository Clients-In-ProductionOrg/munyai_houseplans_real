import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import HousePlan, HousePlanImage

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('s3_upload_tracker')

@receiver(post_save, sender=HousePlan)
def track_houseplan_image_upload(sender, instance, created, **kwargs):
    """Track when HousePlan images are uploaded"""
    if instance.image:
        print(f"\n{'='*70}")
        print(f"[S3 UPLOAD TRACKER] HousePlan Image Saved")
        print(f"{'='*70}")
        print(f"Plan: {instance.name}")
        print(f"Image field: {instance.image.name}")
        print(f"Image URL: {instance.image.url}")
        print(f"Storage: {instance.image.storage.__class__.__name__}")
        print(f"In S3: {'s3' in instance.image.url or 'amazonaws' in instance.image.url}")
        print(f"{'='*70}\n")
        logger.info(f"HousePlan '{instance.name}' image uploaded to: {instance.image.url}")


@receiver(post_save, sender=HousePlanImage)
def track_houseplan_gallery_image_upload(sender, instance, created, **kwargs):
    """Track when HousePlanImage (gallery) images are uploaded"""
    if instance.image:
        print(f"\n{'='*70}")
        print(f"[S3 UPLOAD TRACKER] Gallery Image Saved")
        print(f"{'='*70}")
        print(f"Gallery Image: {instance.image.name}")
        print(f"Image URL: {instance.image.url}")
        print(f"Storage: {instance.image.storage.__class__.__name__}")
        print(f"In S3: {'s3' in instance.image.url or 'amazonaws' in instance.image.url}")
        print(f"{'='*70}\n")
        logger.info(f"Gallery image uploaded to: {instance.image.url}")
