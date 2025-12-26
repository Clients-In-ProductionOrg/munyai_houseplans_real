"""
Admin configuration for core app.
Register models here and configure admin interface.
"""
from django.contrib import admin
from django.contrib.auth.models import User
from decouple import config
from .models import HousePlan, BuiltHome, Contact, Quote, Purchase, SiteSettings, Floor, Feature, Amenity, HousePlanImage


# Customize the admin site
admin.site.site_header = "Cedric House Planning Admin"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to Cedric Admin Dashboard"

# Set the site URL to frontend homepage from environment
admin.site.site_url = config('LOGOUT_REDIRECT_URL')


# Inline admin classes
class FloorInline(admin.TabularInline):
    """Inline admin for floors"""
    model = Floor
    extra = 1
    fields = ('level', 'floor_area', 'bedrooms', 'bathrooms', 'lounges', 'dining_areas', 'notes', 'order')
    ordering = ('order',)


class FeatureInline(admin.TabularInline):
    """Inline admin for features"""
    model = Feature
    extra = 1
    fields = ('name', 'description', 'order')
    ordering = ('order',)


class AmenityInline(admin.TabularInline):
    """Inline admin for amenities"""
    model = Amenity
    extra = 1
    fields = ('name', 'description', 'order')
    ordering = ('order',)


class HousePlanImageInline(admin.TabularInline):
    """Inline admin for multiple house plan images"""
    model = HousePlanImage
    extra = 1
    fields = ('image', 'title', 'order')
    ordering = ('order',)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Admin interface for Site Settings"""
    list_display = ('updated_at',)
    fieldsets = (
        ('YouTube & Media', {
            'fields': ('youtube_link',),
            'description': 'Add YouTube channel or video link here'
        }),
        ('Company Information', {
            'fields': ('company_phone', 'company_email', 'company_address')
        }),
        ('About', {
            'fields': ('about_text',)
        }),
    )
    readonly_fields = ('updated_at',)

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of site settings
        return False

    def has_add_permission(self, request):
        # Only allow one site settings instance
        return not SiteSettings.objects.exists()


@admin.register(HousePlan)
class HousePlanAdmin(admin.ModelAdmin):
    """Admin interface for HousePlan model"""
    list_display = ('name', 'price', 'bedrooms', 'bathrooms', 'garage', 'square_feet', 'is_popular', 'is_best_selling', 'is_new', 'created_at')
    list_filter = ('is_popular', 'is_best_selling', 'is_new', 'pet_friendly', 'bedrooms', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [HousePlanImageInline, FloorInline, FeatureInline, AmenityInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Display Location', {
            'fields': ('display_on',)
        }),
        ('Specifications', {
            'fields': ('bedrooms', 'bathrooms', 'garage', 'square_feet', 'width', 'depth')
        }),
        ('Media & Links', {
            'fields': ('image', 'video_url')
        }),
        ('Features & Status', {
            'fields': ('is_popular', 'is_best_selling', 'is_new', 'pet_friendly')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin interface for Contact model"""
    list_display = ('name', 'email', 'phone', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    """Admin interface for Quote model"""
    list_display = ('name', 'email', 'house_plan', 'is_processed', 'created_at')
    list_filter = ('is_processed', 'house_plan', 'created_at')
    search_fields = ('name', 'email', 'phone', 'requirements')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Requester Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Quote Details', {
            'fields': ('house_plan', 'requirements')
        }),
        ('Status', {
            'fields': ('is_processed',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    """Admin interface for Purchase model"""
    list_display = ('name', 'house_plan', 'plan_price', 'payment_status', 'created_at', 'paid_at')
    list_filter = ('payment_status', 'house_plan', 'created_at', 'paid_at')
    search_fields = ('name', 'email', 'phone', 'yoco_payment_id', 'yoco_reference')
    readonly_fields = ('created_at', 'updated_at', 'yoco_payment_id', 'yoco_reference', 'paid_at')
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone', 'province', 'city', 'pickup_point', 'area_mall')
        }),
        ('Plan Information', {
            'fields': ('house_plan', 'plan_price')
        }),
        ('Payment Information', {
            'fields': ('payment_status', 'yoco_payment_id', 'yoco_reference', 'paid_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )