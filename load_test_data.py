import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim.settings')
django.setup()

from vehicles.models import Driver
from datetime import date, timedelta

# Datos de empleados de prueba
empleados = [
    {
        'full_name': 'Juan Carlos Pérez',
        'license_number': 'A1234567',
        'phone': '5551234567',
        'email': 'juan.perez@icasa.com',
        'address': 'Av. Insurgentes Sur 1234, CDMX',
        'position': 'Chofer',
        'license_expiry': date.today() + timedelta(days=365),
        'hire_date': date(2023, 1, 15),
        'status': 'Activo'
    },
    {
        'full_name': 'María Guadalupe Rodríguez',
        'license_number': 'B2345678',
        'phone': '5552345678',
        'email': 'maria.rodriguez@icasa.com',
        'address': 'Calle Reforma 567, Guadalajara',
        'position': 'Chofer',
        'license_expiry': date.today() + timedelta(days=400),
        'hire_date': date(2022, 6, 10),
        'status': 'Activo'
    },
    {
        'full_name': 'Roberto Sánchez López',
        'license_number': 'C3456789',
        'phone': '5553456789',
        'email': 'roberto.sanchez@icasa.com',
        'address': 'Blvd. Díaz Ordaz 890, Monterrey',
        'position': 'Chofer',
        'license_expiry': date.today() + timedelta(days=300),
        'hire_date': date(2023, 3, 20),
        'status': 'Activo'
    },
    {
        'full_name': 'Ana Patricia Martínez',
        'license_number': 'D4567890',
        'phone': '5554567890',
        'email': 'ana.martinez@icasa.com',
        'address': 'Av. Juárez 345, Puebla',
        'position': 'Supervisor',
        'license_expiry': date.today() + timedelta(days=500),
        'hire_date': date(2021, 9, 5),
        'status': 'Activo'
    },
    {
        'full_name': 'Luis Fernando García',
        'license_number': 'E5678901',
        'phone': '5555678901',
        'email': 'luis.garcia@icasa.com',
        'address': 'Calle Hidalgo 123, Querétaro',
        'position': 'Chofer',
        'license_expiry': date.today() + timedelta(days=450),
        'hire_date': date(2022, 11, 12),
        'status': 'Activo'
    }
]

print("Creando empleados de prueba...")
for emp_data in empleados:
    empleado, created = Driver.objects.get_or_create(
        license_number=emp_data['license_number'],
        defaults=emp_data
    )
    if created:
        print(f"[OK] Creado: {empleado.full_name}")
    else:
        print(f"[--] Ya existe: {empleado.full_name}")

print(f"\nTotal de empleados en la base de datos: {Driver.objects.count()}")
