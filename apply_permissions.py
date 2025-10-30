import os

# Contenido para views_vehicle_documents.py
vehicle_docs_content = """from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Vehicle

class VehicleDocumentsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_documents.html'
    context_object_name = 'vehicles'
    permission_required = 'vehicles.view_document'
    
    def get_queryset(self):
        return Vehicle.objects.prefetch_related('documents__doc_type').all()
"""

# Contenido para views_employee_documents.py
employee_docs_content = """from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Driver

class EmployeeDocumentsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Driver
    template_name = 'vehicles/employee_documents.html'
    context_object_name = 'drivers'
    permission_required = 'vehicles.view_driverdocument'
    
    def get_queryset(self):
        return Driver.objects.prefetch_related('documents').all()
"""

print("Aplicando permisos a documentos vehiculares y empleados...")

with open('vehicles/views_vehicle_documents.py', 'w') as f:
    f.write(vehicle_docs_content)
print("OK - views_vehicle_documents.py actualizado")

with open('vehicles/views_employee_documents.py', 'w') as f:
    f.write(employee_docs_content)
print("OK - views_employee_documents.py actualizado")

print("\nOK - Archivos actualizados localmente")
print("\nAhora debes:")
print("1. Subir estos archivos a PythonAnywhere")
print("2. Reiniciar la aplicacion web")
print("3. Hacer logout y login")
