"""
URL configuration for cedric_admin project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def api_root(request):
    """Root API endpoint"""
    return JsonResponse({
        "message": "Cedric Admin API",
        "version": "1.0",
        "endpoints": {
            "admin": "/admin/",
            "api": "/api/",
            "core": "/api/core/",
            "settings": "/api/core/settings/",
            "house_plans": "/api/core/plans/",
            "contacts": "/api/core/contacts/",
            "quotes": "/api/core/quotes/"
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/core/', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customize admin site
admin.site.site_header = "Cedric Admin Dashboard"
admin.site.site_title = "Cedric Admin"
admin.site.index_title = "Welcome to Cedric Administration"
