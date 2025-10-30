@echo off
echo Subiendo archivos a PythonAnywhere...
echo.

scp vehicles/views_vehicle_documents.py rodrim_dev@ssh.pythonanywhere.com:/home/rodrim_dev/sim_project/vehicles/views_vehicle_documents.py

scp vehicles/views_employee_documents.py rodrim_dev@ssh.pythonanywhere.com:/home/rodrim_dev/sim_project/vehicles/views_employee_documents.py

echo.
echo Archivos subidos. Ahora reiniciando aplicacion...
ssh rodrim_dev@ssh.pythonanywhere.com "touch /var/www/rodrim_dev_pythonanywhere_com_wsgi.py"

echo.
echo Borrando sesiones...
ssh rodrim_dev@ssh.pythonanywhere.com "cd /home/rodrim_dev/sim_project && python manage.py shell -c 'from django.contrib.sessions.models import Session; Session.objects.all().delete(); print(\"Sesiones borradas\")'"

echo.
echo LISTO! Ahora haz logout y login con rodrim_dev
pause
