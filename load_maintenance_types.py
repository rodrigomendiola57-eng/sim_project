import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim.settings')
django.setup()

from vehicles.models import MaintenanceType

maintenance_types = [
    {'name': 'Cambio de Aceite', 'description': 'Cambio de aceite de motor y filtro', 'estimated_cost': 50.00},
    {'name': 'Cambio de Llantas', 'description': 'Reemplazo de neumáticos', 'estimated_cost': 300.00},
    {'name': 'Alineación y Balanceo', 'description': 'Alineación de dirección y balanceo de ruedas', 'estimated_cost': 40.00},
    {'name': 'Revisión de Frenos', 'description': 'Inspección y cambio de pastillas de freno', 'estimated_cost': 80.00},
    {'name': 'Cambio de Batería', 'description': 'Reemplazo de batería del vehículo', 'estimated_cost': 120.00},
    {'name': 'Lavado y Detallado', 'description': 'Limpieza completa interior y exterior', 'estimated_cost': 30.00},
    {'name': 'Revisión General', 'description': 'Inspección completa del vehículo', 'estimated_cost': 60.00},
    {'name': 'Cambio de Filtros', 'description': 'Cambio de filtro de aire y combustible', 'estimated_cost': 35.00},
    {'name': 'Reparación de Motor', 'description': 'Reparación o ajuste del motor', 'estimated_cost': 500.00},
    {'name': 'Cambio de Transmisión', 'description': 'Servicio de transmisión', 'estimated_cost': 200.00},
]

for mt in maintenance_types:
    MaintenanceType.objects.get_or_create(
        name=mt['name'],
        defaults={'description': mt['description'], 'estimated_cost': mt['estimated_cost']}
    )

print(f'Se cargaron {len(maintenance_types)} tipos de mantenimiento')
