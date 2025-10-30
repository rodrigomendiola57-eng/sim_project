import subprocess
import sys

commands = [
    # VehicleDocumentsView
    r"""python manage.py shell -c "
import os
file_path = 'vehicles/views_vehicle_documents.py'
with open(file_path, 'r') as f:
    content = f.read()

new_content = '''from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Vehicle

class VehicleDocumentsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Vehicle
    template_name = \'vehicles/vehicle_documents.html\'
    context_object_name = \'vehicles\'
    permission_required = \'vehicles.view_document\'
    
    def get_queryset(self):
        return Vehicle.objects.prefetch_related(\'documents__doc_type\').all()
'''

with open(file_path, 'w') as f:
    f.write(new_content)
print('VehicleDocumentsView actualizado')
"
""",
    # EmployeeDocumentsView
    r"""python manage.py shell -c "
import os
file_path = 'vehicles/views_employee_documents.py'
with open(file_path, 'r') as f:
    content = f.read()

new_content = '''from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Driver

class EmployeeDocumentsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Driver
    template_name = \'vehicles/employee_documents.html\'
    context_object_name = \'drivers\'
    permission_required = \'vehicles.view_driverdocument\'
    
    def get_queryset(self):
        return Driver.objects.prefetch_related(\'documents\').all()
'''

with open(file_path, 'w') as f:
    f.write(new_content)
print('EmployeeDocumentsView actualizado')
"
""",
    # Reiniciar WSGI
    r"touch /var/www/rodrim_dev_pythonanywhere_com_wsgi.py"
]

print("Ejecutando comandos en PythonAnywhere...")
for i, cmd in enumerate(commands, 1):
    print(f"\n[{i}/{len(commands)}] Ejecutando comando...")
    result = subprocess.run(
        ['ssh', 'rodrim_dev@ssh.pythonanywhere.com', f'cd /home/rodrim_dev/sim_project && {cmd}'],
        capture_output=True,
        text=True
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")

print("\n✓ Proceso completado")
print("IMPORTANTE: Haz logout y login nuevamente para que los cambios surtan efecto")
