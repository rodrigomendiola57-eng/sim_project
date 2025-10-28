from django.views.generic import ListView
from .models import Driver

class EmployeeDocumentsView(ListView):
    model = Driver
    template_name = 'vehicles/employee_documents.html'
    context_object_name = 'drivers'
    
    def get_queryset(self):
        return Driver.objects.prefetch_related('documents').all()
