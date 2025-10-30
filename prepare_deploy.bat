@echo off
echo ========================================
echo Preparando archivos para PythonAnywhere
echo ========================================
echo.

echo Archivos que necesitas subir a PythonAnywhere:
echo.
echo 1. static/css/main.css
echo 2. static/images/ICASA.jpg
echo 3. vehicles/templates/vehicles/base.html
echo 4. vehicles/templates/vehicles/includes/navbar.html
echo.
echo ========================================
echo PASOS A SEGUIR:
echo ========================================
echo.
echo 1. Abre PythonAnywhere en tu navegador
echo 2. Ve a la consola Bash
echo 3. Ejecuta estos comandos:
echo.
echo    cd ~/rodrigomendiola.pythonanywhere.com
echo    rm -f vehicles/static/css/main.css
echo    python manage.py collectstatic --noinput --clear
echo.
echo 4. Ve a la pestana Web
echo 5. Click en "Reload rodrigomendiola.pythonanywhere.com"
echo 6. Abre tu sitio y presiona Ctrl+Shift+R
echo.
echo ========================================
echo.
pause
