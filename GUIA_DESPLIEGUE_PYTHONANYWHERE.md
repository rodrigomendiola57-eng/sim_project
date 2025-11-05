# 🚀 GUÍA DE DESPLIEGUE A PYTHONANYWHERE

## ✅ CAMBIOS LISTOS PARA DESPLEGAR

### Dashboard
- ✅ Cards animados con contadores
- ✅ Gráficos Chart.js (doughnut y bar)
- ✅ Hero section con gradiente ICASA
- ✅ Altura fija en gráficos

### Módulo Vehículos - Fase 1
- ✅ Vista Cards/Tabla con toggle
- ✅ Filtros avanzados (búsqueda, estación, estado, año)
- ✅ Hover effects y badges con gradientes
- ✅ Paginación de 50 elementos

### Módulo Vehículos - Fase 2
- ✅ Exportar a Excel
- ✅ Exportar a PDF
- ✅ Importar desde Excel
- ✅ Historial del vehículo (timeline)
- ✅ Código QR por vehículo

### Mejoras UI
- ✅ Botones alineados con Flexbox
- ✅ Filtro con 32 estados de México
- ✅ QR único con ID del vehículo
- ✅ Modal para ver QR en web

### Checklists
- ✅ Apartado en detalle de vehículo
- ✅ Modal para crear checklist
- ✅ Formulario de 19 puntos

### Dependencias Nuevas
- ✅ openpyxl (Excel)
- ✅ reportlab (PDF)
- ✅ qrcode (QR codes)

---

## 📋 PASOS PARA DESPLEGAR

### OPCIÓN 1: Usando Script Automático (Recomendado)

#### Paso 1: Conectar a PythonAnywhere
```bash
# Ir a: https://www.pythonanywhere.com/
# Login con tu cuenta
# Click en "Consoles" → "Bash"
```

#### Paso 2: Ejecutar Script de Despliegue
```bash
cd /home/RodrigoMendiola/sim_project
git pull origin main
pip install --user openpyxl reportlab qrcode[pil]
python manage.py migrate
python manage.py collectstatic --noinput
touch /var/www/rodrigomendiola_pythonanywhere_com_wsgi.py
```

#### Paso 3: Verificar
```
Visitar: https://rodrigomendiola.pythonanywhere.com
```

---

### OPCIÓN 2: Paso a Paso Manual

#### 1️⃣ Abrir Consola Bash en PythonAnywhere
```
https://www.pythonanywhere.com/user/RodrigoMendiola/consoles/
Click en "Bash"
```

#### 2️⃣ Navegar al Proyecto
```bash
cd /home/RodrigoMendiola/sim_project
```

#### 3️⃣ Descargar Cambios desde GitHub
```bash
git pull origin main
```

**Salida esperada:**
```
Updating 55d2fae..9a3cb3b
Fast-forward
 CHECKLIST_EN_DETALLE_VEHICULO.md          | 354 +++++++++++++++++
 GUIA_RAPIDA_VEHICULOS.md                  | 266 +++++++++++++
 MEJORAS_UI_VEHICULOS.md                   | 360 +++++++++++++++++
 MODULO_VEHICULOS_AVANZADO.md              | 371 +++++++++++++++++
 RESUMEN_MODULO_VEHICULOS.md               | 371 +++++++++++++++++
 requirements.txt                           |   3 +
 vehicles/templates/vehicles/dashboard_new.html | 200 ++++++++++
 vehicles/templates/vehicles/vehicle_detail.html | 330 +++++++++++++++
 vehicles/templates/vehicles/vehicle_history.html | 200 ++++++++++
 vehicles/templates/vehicles/vehicle_list_new.html | 400 +++++++++++++++++++
 vehicles/urls.py                          |   8 +
 vehicles/views.py                         |   3 +
 vehicles/views_checklist.py               |   5 +
 vehicles/views_dashboard.py               |   2 +
 vehicles/views_vehicle_advanced.py        | 350 ++++++++++++++++
 15 files changed, 3223 insertions(+)
```

#### 4️⃣ Instalar Nuevas Dependencias
```bash
pip install --user openpyxl reportlab qrcode[pil]
```

**Salida esperada:**
```
Successfully installed openpyxl-3.1.5 reportlab-4.4.4 qrcode-8.2
```

#### 5️⃣ Aplicar Migraciones (si hay)
```bash
python manage.py migrate
```

**Salida esperada:**
```
Operations to perform:
  Apply all migrations: ...
Running migrations:
  No migrations to apply.
```

#### 6️⃣ Recolectar Archivos Estáticos
```bash
python manage.py collectstatic --noinput
```

**Salida esperada:**
```
X static files copied to '/home/RodrigoMendiola/sim_project/staticfiles'
```

#### 7️⃣ Recargar Aplicación Web
```bash
touch /var/www/rodrigomendiola_pythonanywhere_com_wsgi.py
```

O desde la interfaz web:
```
Web → rodrigomendiola.pythonanywhere.com → Reload
```

---

## ✅ VERIFICACIÓN

### 1. Dashboard
```
URL: https://rodrigomendiola.pythonanywhere.com/
```
**Verificar:**
- ✅ Cards con contadores animados
- ✅ Gráfico de dona (estado de vehículos)
- ✅ Gráfico de barras (mantenimientos)
- ✅ Hero section verde

### 2. Lista de Vehículos
```
URL: https://rodrigomendiola.pythonanywhere.com/vehicles/
```
**Verificar:**
- ✅ Toggle Cards/Tabla funciona
- ✅ Botones alineados (Cards|Tabla, Exportar, Importar, Agregar)
- ✅ Filtro de estación con 32 estados
- ✅ Vista de cards con fotos grandes
- ✅ Hover effects en cards

### 3. Exportar/Importar
```
URL: https://rodrigomendiola.pythonanywhere.com/vehicles/
```
**Verificar:**
- ✅ Click en "Exportar" → "Exportar a Excel" descarga archivo
- ✅ Click en "Exportar" → "Exportar a PDF" descarga archivo
- ✅ Click en "Importar" abre modal
- ✅ Descargar plantilla funciona

### 4. Detalle de Vehículo
```
URL: https://rodrigomendiola.pythonanywhere.com/vehicles/<id>/
```
**Verificar:**
- ✅ Botón "Historial" funciona
- ✅ Botón "Ver QR" abre modal
- ✅ QR se muestra en modal
- ✅ Botón "Descargar QR" funciona
- ✅ Sección de Checklists visible
- ✅ Botón "Nuevo Checklist" abre modal

### 5. Historial del Vehículo
```
URL: https://rodrigomendiola.pythonanywhere.com/vehicles/<id>/history/
```
**Verificar:**
- ✅ Timeline vertical se muestra
- ✅ Eventos ordenados por fecha
- ✅ Iconos y colores correctos
- ✅ Información completa

### 6. Crear Checklist
```
URL: Desde detalle del vehículo → "Nuevo Checklist"
```
**Verificar:**
- ✅ Modal se abre
- ✅ Formulario completo (19 puntos)
- ✅ Dropdown con 32 estados
- ✅ Guardar funciona
- ✅ Redirecciona al detalle

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: "No module named 'openpyxl'"
```bash
pip install --user openpyxl reportlab qrcode[pil]
```

### Error: "No such file or directory"
```bash
cd /home/RodrigoMendiola/sim_project
pwd  # Verificar ruta
```

### Error: "Permission denied"
```bash
# Usar --user en pip install
pip install --user nombre_paquete
```

### Cambios no se ven
```bash
# Limpiar caché del navegador
# O abrir en ventana incógnito
# O hacer Ctrl+F5 (hard refresh)
```

### Error en git pull
```bash
# Si hay conflictos
git stash
git pull origin main
git stash pop
```

### Aplicación no recarga
```bash
# Método 1: Touch WSGI
touch /var/www/rodrigomendiola_pythonanywhere_com_wsgi.py

# Método 2: Desde Web UI
# Web → Reload button (verde)
```

---

## 📊 CHECKLIST DE DESPLIEGUE

```
[ ] 1. Push a GitHub completado
[ ] 2. Conectado a PythonAnywhere Bash
[ ] 3. Navegado a /home/RodrigoMendiola/sim_project
[ ] 4. git pull ejecutado exitosamente
[ ] 5. Dependencias instaladas (openpyxl, reportlab, qrcode)
[ ] 6. Migraciones aplicadas
[ ] 7. Archivos estáticos recolectados
[ ] 8. Aplicación recargada
[ ] 9. Dashboard verificado
[ ] 10. Lista de vehículos verificada
[ ] 11. Exportar/Importar verificado
[ ] 12. Detalle de vehículo verificado
[ ] 13. Historial verificado
[ ] 14. QR modal verificado
[ ] 15. Checklists verificado
```

---

## 🎯 COMANDOS RÁPIDOS

### Despliegue Completo (Copiar y Pegar)
```bash
cd /home/RodrigoMendiola/sim_project && \
git pull origin main && \
pip install --user openpyxl reportlab qrcode[pil] && \
python manage.py migrate && \
python manage.py collectstatic --noinput && \
touch /var/www/rodrigomendiola_pythonanywhere_com_wsgi.py && \
echo "✅ Despliegue completado!"
```

### Ver Logs de Error
```bash
tail -f /var/log/rodrigomendiola.pythonanywhere.com.error.log
```

### Ver Logs de Servidor
```bash
tail -f /var/log/rodrigomendiola.pythonanywhere.com.server.log
```

---

## 📞 SOPORTE

### Si algo falla:
1. Revisar logs de error
2. Verificar que git pull funcionó
3. Verificar que dependencias se instalaron
4. Recargar aplicación nuevamente
5. Limpiar caché del navegador

### Contacto PythonAnywhere:
- Help: https://help.pythonanywhere.com/
- Forum: https://www.pythonanywhere.com/forums/

---

## ✨ RESULTADO ESPERADO

Después del despliegue, tu sitio en:
```
https://rodrigomendiola.pythonanywhere.com
```

Debe mostrar:
- ✅ Dashboard moderno con gráficos
- ✅ Vehículos con vista cards/tabla
- ✅ Exportar/Importar Excel y PDF
- ✅ Historial con timeline
- ✅ QR codes en modal
- ✅ Checklists integrados
- ✅ Filtros con 32 estados
- ✅ Botones perfectamente alineados

---

**Última actualización:** Enero 2025  
**Commits desplegados:** 12 commits  
**Archivos nuevos:** 8 archivos  
**Líneas de código:** ~3,200 líneas
