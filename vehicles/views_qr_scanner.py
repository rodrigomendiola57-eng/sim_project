from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Vehicle

class QRScannerView(LoginRequiredMixin, TemplateView):
    template_name = 'vehicles/qr_scanner.html'

class QRLookupView(LoginRequiredMixin, TemplateView):
    """Vista para buscar vehículo por ID escaneado del QR"""
    
    def get(self, request, *args, **kwargs):
        vehicle_id = request.GET.get('id')
        
        if not vehicle_id:
            return JsonResponse({'error': 'No se proporcionó ID de vehículo'}, status=400)
        
        try:
            vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
            return JsonResponse({
                'success': True,
                'vehicle_id': vehicle.id,
                'plate': vehicle.plate,
                'brand': vehicle.brand,
                'model': vehicle.model,
                'url': f'/vehicles/{vehicle.id}/'
            })
        except:
            return JsonResponse({'error': 'Vehículo no encontrado'}, status=404)
