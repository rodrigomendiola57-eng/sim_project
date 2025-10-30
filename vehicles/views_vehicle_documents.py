from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Vehicle

class VehicleDocumentsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_documents.html'
    context_object_name = 'vehicles'
    permission_required = 'vehicles.view_document'
    
    def get_queryset(self):
        return Vehicle.objects.prefetch_related('documents__doc_type').all()
