import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim.settings')
django.setup()

from vehicles.models import DocumentType

document_types = [
    {'name': 'Tarjeta de Circulación', 'description': 'Documento que acredita la propiedad del vehículo', 'validity_months': 12, 'is_required': True},
    {'name': 'Verificación Vehicular', 'description': 'Constancia de verificación de emisiones contaminantes', 'validity_months': 6, 'is_required': True},
    {'name': 'Tenencia', 'description': 'Impuesto sobre tenencia o uso de vehículos', 'validity_months': 12, 'is_required': True},
    {'name': 'Seguro de Responsabilidad Civil', 'description': 'Póliza de seguro obligatorio', 'validity_months': 12, 'is_required': True},
    {'name': 'Licencia de Conducir', 'description': 'Licencia vigente del conductor', 'validity_months': 36, 'is_required': True},
    {'name': 'Placas', 'description': 'Placas de circulación vigentes', 'validity_months': 60, 'is_required': True},
    {'name': 'Permiso SCT', 'description': 'Permiso de la Secretaría de Comunicaciones y Transportes', 'validity_months': 12, 'is_required': False},
    {'name': 'Revista Mecánica', 'description': 'Revisión técnico-mecánica del vehículo', 'validity_months': 12, 'is_required': False},
    {'name': 'Póliza de Seguro Amplia', 'description': 'Seguro de cobertura amplia (opcional)', 'validity_months': 12, 'is_required': False},
]

for dt in document_types:
    DocumentType.objects.get_or_create(
        name=dt['name'],
        defaults={
            'description': dt['description'],
            'validity_months': dt['validity_months'],
            'is_required': dt['is_required']
        }
    )

print(f'Se cargaron {len(document_types)} tipos de documentos')
