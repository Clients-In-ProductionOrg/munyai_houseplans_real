"""
Core app views
"""
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from .models import HousePlan, BuiltHome, Contact, Quote, Purchase, SiteSettings
from . import serializers


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_site_settings(request):
    """Endpoint to get site settings (public access)"""
    try:
        settings = SiteSettings.objects.first()
        if settings:
            serializer = serializers.SiteSettingsSerializer(settings)
            return Response(serializer.data)
        return Response({
            'youtube_link': None,
            'company_phone': None,
            'company_email': None,
            'company_address': None,
            'about_text': None
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HousePlanViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing house plans"""
    queryset = HousePlan.objects.all()
    serializer_class = serializers.HousePlanSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['is_popular', 'bedrooms', 'display_on']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']


class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet for contact messages"""
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class QuoteViewSet(viewsets.ModelViewSet):
    """ViewSet for quote requests"""
    queryset = Quote.objects.all()
    serializer_class = serializers.QuoteSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class PurchaseViewSet(viewsets.ModelViewSet):
    """ViewSet for purchases and payments"""
    queryset = Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['payment_status', 'house_plan']
    search_fields = ['name', 'email', 'yoco_payment_id']
    ordering_fields = ['created_at', 'paid_at']

    def perform_create(self, serializer):
        serializer.save()
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
    def update_payment_status(self, request, pk=None):
        """Endpoint to update payment status from Yoco"""
        purchase = self.get_object()
        payment_status = request.data.get('payment_status')
        yoco_payment_id = request.data.get('yoco_payment_id')
        yoco_reference = request.data.get('yoco_reference')
        
        if payment_status:
            purchase.payment_status = payment_status
        if yoco_payment_id:
            purchase.yoco_payment_id = yoco_payment_id
        if yoco_reference:
            purchase.yoco_reference = yoco_reference
        
        if payment_status == 'completed':
            from django.utils import timezone
            purchase.paid_at = timezone.now()
        
        purchase.save()
        
        serializer = self.get_serializer(purchase)
        return Response(serializer.data)