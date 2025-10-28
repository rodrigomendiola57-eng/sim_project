from django.views.generic import ListView
from .models import Vehicle

class VehicleDocumentsView(ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_documents.html'
    context_object_name = 'vehicles'
    
    def get_queryset(self):
        return Vehicle.objects.prefetch_related('documents__doc_type').all()
