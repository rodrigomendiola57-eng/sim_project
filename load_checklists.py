import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim.settings')
django.setup()

from vehicles.models import VehicleChecklist, Vehicle, Driver

# Verificar que existan vehículos
vehicles = list(Vehicle.objects.all())
if not vehicles:
    print("Error: No hay vehículos en la base de datos. Crea vehículos primero.")
    exit()

# Obtener nombres de conductores
drivers = list(Driver.objects.all())
driver_names = [d.full_name for d in drivers] if drivers else ['Juan Pérez', 'María López', 'Carlos García']

# Datos de checklists de prueba
checklists_data = [
    {
        'vehicle': random.choice(vehicles),
        'driver_name': random.choice(driver_names),
        'tires_condition': 'Bueno',
        'tires_pressure': 'Bueno',
        'lights': 'Bueno',
        'mirrors': 'Bueno',
        'windshield': 'Bueno',
        'wipers': 'Bueno',
        'body_damage': 'Bueno',
        'seat_belts': 'Bueno',
        'horn': 'Bueno',
        'dashboard_lights': 'Bueno',
        'air_conditioning': 'Bueno',
        'brakes': 'Bueno',
        'engine': 'Bueno',
        'oil_level': 'Bueno',
        'coolant_level': 'Bueno',
        'battery': 'Bueno',
        'fire_extinguisher': 'Bueno',
        'first_aid_kit': 'Bueno',
        'warning_triangles': 'Bueno',
        'odometer_reading': 45000,
        'fuel_level': 'Lleno',
        'observations': 'Vehículo en excelente estado, listo para operación.'
    },
    {
        'vehicle': random.choice(vehicles),
        'driver_name': random.choice(driver_names),
        'tires_condition': 'Bueno',
        'tires_pressure': 'Regular',
        'lights': 'Bueno',
        'mirrors': 'Bueno',
        'windshield': 'Regular',
        'wipers': 'Regular',
        'body_damage': 'Bueno',
        'seat_belts': 'Bueno',
        'horn': 'Bueno',
        'dashboard_lights': 'Bueno',
        'air_conditioning': 'Bueno',
        'brakes': 'Bueno',
        'engine': 'Bueno',
        'oil_level': 'Bueno',
        'coolant_level': 'Bueno',
        'battery': 'Bueno',
        'fire_extinguisher': 'Bueno',
        'first_aid_kit': 'Bueno',
        'warning_triangles': 'Bueno',
        'odometer_reading': 52300,
        'fuel_level': '3/4',
        'observations': 'Presión de llantas baja, parabrisas con pequeñas grietas. Requiere atención.'
    },
    {
        'vehicle': random.choice(vehicles),
        'driver_name': random.choice(driver_names),
        'tires_condition': 'Regular',
        'tires_pressure': 'Regular',
        'lights': 'Malo',
        'mirrors': 'Bueno',
        'windshield': 'Bueno',
        'wipers': 'Bueno',
        'body_damage': 'Regular',
        'seat_belts': 'Bueno',
        'horn': 'Bueno',
        'dashboard_lights': 'Bueno',
        'air_conditioning': 'Regular',
        'brakes': 'Bueno',
        'engine': 'Bueno',
        'oil_level': 'Regular',
        'coolant_level': 'Bueno',
        'battery': 'Bueno',
        'fire_extinguisher': 'Bueno',
        'first_aid_kit': 'Bueno',
        'warning_triangles': 'Bueno',
        'odometer_reading': 78500,
        'fuel_level': '1/2',
        'observations': 'Luz delantera derecha fundida. Llantas desgastadas. Programar mantenimiento.'
    },
    {
        'vehicle': random.choice(vehicles),
        'driver_name': random.choice(driver_names),
        'tires_condition': 'Bueno',
        'tires_pressure': 'Bueno',
        'lights': 'Bueno',
        'mirrors': 'Bueno',
        'windshield': 'Bueno',
        'wipers': 'Bueno',
        'body_damage': 'Bueno',
        'seat_belts': 'Bueno',
        'horn': 'Bueno',
        'dashboard_lights': 'Bueno',
        'air_conditioning': 'Bueno',
        'brakes': 'Bueno',
        'engine': 'Bueno',
        'oil_level': 'Bueno',
        'coolant_level': 'Bueno',
        'battery': 'Bueno',
        'fire_extinguisher': 'Bueno',
        'first_aid_kit': 'Bueno',
        'warning_triangles': 'Bueno',
        'odometer_reading': 32100,
        'fuel_level': 'Lleno',
        'observations': 'Unidad nueva, todo en perfecto estado.'
    },
    {
        'vehicle': random.choice(vehicles),
        'driver_name': random.choice(driver_names),
        'tires_condition': 'Bueno',
        'tires_pressure': 'Bueno',
        'lights': 'Bueno',
        'mirrors': 'Regular',
        'windshield': 'Bueno',
        'wipers': 'Regular',
        'body_damage': 'Bueno',
        'seat_belts': 'Bueno',
        'horn': 'Bueno',
        'dashboard_lights': 'Bueno',
        'air_conditioning': 'Malo',
        'brakes': 'Bueno',
        'engine': 'Bueno',
        'oil_level': 'Bueno',
        'coolant_level': 'Regular',
        'battery': 'Bueno',
        'fire_extinguisher': 'Bueno',
        'first_aid_kit': 'Bueno',
        'warning_triangles': 'Bueno',
        'odometer_reading': 61200,
        'fuel_level': '1/4',
        'observations': 'Aire acondicionado no funciona. Espejo retrovisor flojo. Requiere reparación urgente.'
    }
]

print("Creando checklists de prueba...")
created_count = 0
for checklist_data in checklists_data:
    checklist = VehicleChecklist.objects.create(**checklist_data)
    print(f"[OK] Creado checklist para {checklist.vehicle.plate} - Conductor: {checklist.driver_name} - Estado: {checklist.overall_status}")
    created_count += 1

print(f"\nTotal de checklists creados: {created_count}")
print(f"Total de checklists en la base de datos: {VehicleChecklist.objects.count()}")
