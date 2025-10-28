# Proyecto SIM_Project

Este proyecto es un **CRUD completo de vehículos, documentos y mantenimientos** desarrollado con **Django 5.2** y Python 3.13. Permite a los usuarios agregar, editar, eliminar y listar información de vehículos, documentos y mantenimientos.

---

## Características

- ✅ CRUD completo para Vehículos, Documentos y Mantenimientos
- ✅ Validación de formularios
- ✅ Paginación (10 items por página)
- ✅ Mensajes de éxito/error
- ✅ Panel de administración mejorado
- ✅ Optimización de consultas con select_related
- ✅ Índices de base de datos para mejor rendimiento
- ✅ Configuración de seguridad para producción

---

## Requisitos

- Python 3.13
- Django 5.2.7
- pip

---

## Instalación

1. **Clonar el repositorio**
```bash
cd sim_project
```

2. **Crear entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno (opcional)**
```bash
copy .env.example .env
# Editar .env con tus valores
```

5. **Ejecutar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

---

## Cómo correr el proyecto

1. Abrir la terminal en la carpeta del proyecto (`sim_project`) y ejecutar:
```bash
python manage.py runserver
```

2. Abrir el navegador y acceder a las siguientes URLs:

- **Vehículos**: http://127.0.0.1:8000/vehicles/
- **Documentos**: http://127.0.0.1:8000/vehicles/documents/
- **Mantenimientos**: http://127.0.0.1:8000/vehicles/maintenance/
- **Panel de administrador**: http://127.0.0.1:8000/admin/

---

## Estructura del Proyecto

```
sim_project/
├── sim/                    # Configuración principal
│   ├── settings.py        # Configuración con variables de entorno
│   └── urls.py
├── vehicles/              # App principal
│   ├── models.py         # Modelos con validaciones
│   ├── views.py          # Vistas con paginación
│   ├── forms.py          # Formularios personalizados
│   ├── admin.py          # Admin mejorado
│   └── templates/
├── logs/                  # Logs de errores
├── .env.example          # Ejemplo de variables de entorno
└── requirements.txt      # Dependencias
```

---

## Mejoras Implementadas

### Seguridad
- Variables de entorno para SECRET_KEY y DEBUG
- Configuración de seguridad para producción
- Validaciones en modelos y formularios

### Rendimiento
- Índices en campos frecuentemente consultados
- select_related para optimizar consultas
- Paginación en todas las listas

### Usabilidad
- Mensajes de éxito/error
- Panel de administración mejorado
- Formularios con validación personalizada
- Campos con verbose_name en español

---

## Próximas Mejoras Sugeridas

- [ ] Agregar tests unitarios
- [ ] Implementar autenticación de usuarios
- [ ] Agregar filtros en las listas
- [ ] Exportar datos a Excel/PDF
- [ ] Dashboard con estadísticas
- [ ] API REST con Django REST Framework
