"""
Script de prueba para verificar las funcionalidades avanzadas del módulo de vehículos
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim.settings')
django.setup()

from vehicles.models import Vehicle, Maintenance, Document
from datetime import datetime

def test_vehicle_data():
    """Verifica que hay datos de vehículos para probar"""
    vehicles = Vehicle.objects.all()
    print(f"[OK] Total de vehiculos: {vehicles.count()}")
    
    if vehicles.exists():
        vehicle = vehicles.first()
        print(f"   Ejemplo: {vehicle.plate} - {vehicle.brand} {vehicle.model}")
        
        # Verificar mantenimientos
        maintenances = Maintenance.objects.filter(vehicle=vehicle)
        print(f"   Mantenimientos: {maintenances.count()}")
        
        # Verificar documentos
        documents = Document.objects.filter(vehicle=vehicle)
        print(f"   Documentos: {documents.count()}")
        
        return True
    else:
        print("[WARN] No hay vehiculos en la base de datos")
        return False

def test_imports():
    """Verifica que las librerías necesarias están instaladas"""
    try:
        import openpyxl
        print("[OK] openpyxl instalado correctamente")
    except ImportError:
        print("[ERROR] openpyxl NO instalado")
        return False
    
    try:
        import reportlab
        print("[OK] reportlab instalado correctamente")
    except ImportError:
        print("[ERROR] reportlab NO instalado")
        return False
    
    try:
        import qrcode
        print("[OK] qrcode instalado correctamente")
    except ImportError:
        print("[ERROR] qrcode NO instalado")
        return False
    
    return True

def test_views():
    """Verifica que las vistas están correctamente importadas"""
    try:
        from vehicles.views_vehicle_advanced import (
            VehicleExportExcelView,
            VehicleExportPDFView,
            VehicleImportExcelView,
            VehicleHistoryView,
            VehicleQRCodeView,
            VehicleDownloadTemplateView
        )
        print("[OK] Todas las vistas avanzadas importadas correctamente")
        return True
    except ImportError as e:
        print(f"[ERROR] Error al importar vistas: {e}")
        return False

def main():
    print("=" * 60)
    print("PRUEBA DE FUNCIONALIDADES AVANZADAS - MODULO VEHICULOS")
    print("=" * 60)
    print()
    
    print("[1] Verificando librerias...")
    if not test_imports():
        print("\n[ERROR] Faltan librerias. Ejecutar: pip install openpyxl reportlab qrcode[pil]")
        return
    print()
    
    print("[2] Verificando vistas...")
    if not test_views():
        print("\n[ERROR] Error en las vistas")
        return
    print()
    
    print("[3] Verificando datos...")
    if not test_vehicle_data():
        print("\n[WARN] Considera agregar vehiculos de prueba")
    print()
    
    print("=" * 60)
    print("TODAS LAS VERIFICACIONES COMPLETADAS")
    print("=" * 60)
    print()
    print("URLs disponibles:")
    print("   - Exportar Excel: /vehicles/export/excel/")
    print("   - Exportar PDF: /vehicles/export/pdf/")
    print("   - Importar Excel: /vehicles/import/excel/")
    print("   - Descargar Plantilla: /vehicles/template/download/")
    print("   - Historial: /vehicles/<id>/history/")
    print("   - QR Code: /vehicles/<id>/qr/")
    print()
    print("Servidor listo para probar las funcionalidades!")
    print("   Ejecutar: python manage.py runserver")

if __name__ == "__main__":
    main()
