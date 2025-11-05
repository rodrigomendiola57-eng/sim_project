#!/bin/bash
# Script para desplegar cambios en PythonAnywhere

echo "=========================================="
echo "DESPLEGANDO CAMBIOS A PYTHONANYWHERE"
echo "=========================================="
echo ""

# 1. Ir al directorio del proyecto
echo "[1/6] Navegando al directorio del proyecto..."
cd /home/RodrigoMendiola/sim_project

# 2. Hacer pull de los cambios
echo "[2/6] Descargando cambios desde GitHub..."
git pull origin main

# 3. Instalar nuevas dependencias
echo "[3/6] Instalando nuevas dependencias..."
pip install --user openpyxl reportlab qrcode[pil]

# 4. Aplicar migraciones
echo "[4/6] Aplicando migraciones de base de datos..."
python manage.py migrate

# 5. Recolectar archivos estáticos
echo "[5/6] Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# 6. Recargar aplicación web
echo "[6/6] Recargando aplicación web..."
touch /var/www/rodrigomendiola_pythonanywhere_com_wsgi.py

echo ""
echo "=========================================="
echo "✅ DESPLIEGUE COMPLETADO"
echo "=========================================="
echo ""
echo "Cambios desplegados:"
echo "- Dashboard mejorado con gráficos"
echo "- Módulo Vehículos Fase 1: Vista cards/tabla"
echo "- Módulo Vehículos Fase 2: Exportar/Importar/Historial/QR"
echo "- Mejoras UI: Botones alineados, 32 estados, QR modal"
echo "- Checklists integrados en detalle de vehículo"
echo ""
echo "Visita: https://rodrigomendiola.pythonanywhere.com"
