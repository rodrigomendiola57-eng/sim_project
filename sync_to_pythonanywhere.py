"""
Script para sincronizar archivos a PythonAnywhere manualmente
Copia este contenido y pégalo en los archivos correspondientes en PythonAnywhere
"""

print("="*80)
print("INSTRUCCIONES PARA ACTUALIZAR PYTHONANYWHERE")
print("="*80)
print()
print("1. Ve a https://www.pythonanywhere.com/")
print("2. Inicia sesión")
print("3. Ve a 'Files'")
print("4. Navega a: /home/RodrigoMendiola/sim_project")
print()
print("="*80)
print("ARCHIVOS A ACTUALIZAR:")
print("="*80)
print()

# Leer y mostrar cada archivo
import os

files_to_sync = [
    'vehicles/models.py',
    'vehicles/views.py', 
    'vehicles/urls.py',
    'vehicles/forms.py',
    'vehicles/templates/vehicles/vehicle_list.html',
    'vehicles/templates/vehicles/vehicle_detail.html'
]

for file_path in files_to_sync:
    full_path = os.path.join(r'C:\sim_project', file_path)
    if os.path.exists(full_path):
        print(f"\n{'='*80}")
        print(f"ARCHIVO: {file_path}")
        print('='*80)
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    else:
        print(f"\n⚠️  ARCHIVO NO ENCONTRADO: {file_path}")

print("\n" + "="*80)
print("DESPUÉS DE COPIAR LOS ARCHIVOS, EJECUTA EN LA CONSOLA BASH:")
print("="*80)
print("""
cd /home/RodrigoMendiola/sim_project
python manage.py makemigrations
python manage.py migrate
""")
print("\nLuego ve a la pestaña 'Web' y haz clic en 'Reload'")
print("="*80)
