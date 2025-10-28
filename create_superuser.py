import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='Rodrigo').exists():
    User.objects.create_superuser('Rodrigo', 'rodrigomendiola57@gmail.com', 'Mendiola123')
    print('Superusuario creado exitosamente')
else:
    print('El usuario ya existe')
