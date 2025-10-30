from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Driver

class EmployeeDocumentsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Driver
    template_name = 'vehicles/employee_documents.html'
    context_object_name = 'drivers'
    permission_required = 'vehicles.view_driverdocument'
    
    def get_queryset(self):
        return Driver.objects.prefetch_related('documents').all()
