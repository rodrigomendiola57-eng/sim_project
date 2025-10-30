@echo off
echo ========================================
echo Reiniciando servidor con cambios...
echo ========================================
echo.
echo 1. Recolectando archivos estaticos...
python manage.py collectstatic --noinput --clear
echo.
echo 2. Iniciando servidor...
echo.
echo IMPORTANTE: Abre tu navegador y presiona Ctrl+Shift+R para forzar recarga
echo.
python manage.py runserver
