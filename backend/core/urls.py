"""
Core app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'plans', views.HousePlanViewSet, basename='houseplan')
router.register(r'contacts', views.ContactViewSet, basename='contact')
router.register(r'quotes', views.QuoteViewSet, basename='quote')
router.register(r'purchases', views.PurchaseViewSet, basename='purchase')
urlpatterns = [
    path('', include(router.urls)),
    path('settings/', views.get_site_settings, name='site-settings'),
]