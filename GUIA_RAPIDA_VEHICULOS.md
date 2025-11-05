# 🚗 GUÍA RÁPIDA - MÓDULO VEHÍCULOS

## 🎯 ACCESO RÁPIDO

### 📍 URLs Principales
```
http://127.0.0.1:8000/vehicles/              → Lista de vehículos
http://127.0.0.1:8000/vehicles/<id>/         → Detalle
http://127.0.0.1:8000/vehicles/<id>/history/ → Historial
```

---

## ⚡ FUNCIONES PRINCIPALES

### 1️⃣ VER VEHÍCULOS
**Ubicación:** `/vehicles/`

**Opciones de vista:**
- 🎴 **Cards:** Vista con fotos grandes y diseño moderno
- 📊 **Tabla:** Vista compacta tipo lista

**Cambiar vista:** Click en botones "Cards" o "Tabla" (se guarda tu preferencia)

---

### 2️⃣ FILTRAR VEHÍCULOS
**Ubicación:** `/vehicles/` → Panel de filtros

**Filtros disponibles:**
- 🔍 **Búsqueda:** Por placa, marca o modelo
- 📍 **Estación:** Filtrar por ubicación
- 🏷️ **Estado:** Activo, Mantenimiento, Fuera de Servicio
- 📅 **Año:** Filtrar por año del vehículo

**Uso:**
1. Llenar los campos deseados
2. Click en "Filtrar"
3. Para limpiar: Click en ❌

---

### 3️⃣ EXPORTAR DATOS
**Ubicación:** `/vehicles/` → Botón "Exportar"

#### 📊 Exportar a Excel
1. Aplicar filtros (opcional)
2. Click en "Exportar" → "Exportar a Excel"
3. Archivo `.xlsx` se descarga automáticamente
4. Abrir con Excel/LibreOffice

#### 📄 Exportar a PDF
1. Aplicar filtros (opcional)
2. Click en "Exportar" → "Exportar a PDF"
3. Archivo `.pdf` se descarga automáticamente
4. Abrir con lector PDF

**💡 Tip:** Los filtros aplicados se respetan en la exportación

---

### 4️⃣ IMPORTAR VEHÍCULOS
**Ubicación:** `/vehicles/` → Botón "Importar"

**Pasos:**
1. Click en "Importar"
2. (Opcional) Descargar plantilla Excel
3. Llenar Excel con datos:
   ```
   Placa | Marca | Modelo | Año | Estado | Estación
   ```
4. Subir archivo en el modal
5. Esperar resultado
6. Página se recarga automáticamente

**Formato de ejemplo:**
```
ABC-123 | Toyota | Hilux | 2023 | Active | Ciudad de México
XYZ-789 | Ford | Ranger | 2022 | Active | Jalisco
```

**Estados válidos:**
- `Active`
- `Maintenance`
- `Out of service`

**💡 Tip:** Si la placa ya existe, se actualiza el vehículo

---

### 5️⃣ VER HISTORIAL
**Ubicación:** Detalle del vehículo → Botón "Historial"

**Qué muestra:**
- 🔧 Todos los mantenimientos realizados
- 📄 Todos los documentos registrados
- 📅 Orden cronológico (más reciente primero)

**Información de mantenimientos:**
- Tipo de servicio
- Estado actual
- Costo (real o estimado)
- Taller asignado
- Descripción del problema

**Información de documentos:**
- Tipo de documento
- Estado (Vigente/Expirado)
- Fecha de vencimiento
- Número de documento

---

### 6️⃣ GENERAR QR CODE
**Ubicación:** Detalle del vehículo → Botón "QR Code"

**Pasos:**
1. Entrar al detalle de un vehículo
2. Click en "QR Code"
3. Imagen PNG se descarga automáticamente
4. Imprimir la imagen
5. Pegar en el vehículo

**Información en el QR:**
- Placa
- Marca y Modelo
- Año
- Estado
- Estación

**💡 Uso sugerido:** Pegar en el parabrisas o puerta del vehículo

---

## 🎨 ESTADOS DE VEHÍCULOS

### 🟢 Activo (Active)
- Vehículo operativo
- Disponible para uso
- Color: Verde

### 🟡 Mantenimiento (Maintenance)
- En taller o servicio
- No disponible temporalmente
- Color: Amarillo/Naranja

### 🔴 Fuera de Servicio (Out of service)
- No operativo
- Requiere reparación mayor
- Color: Rojo

---

## 📋 ATAJOS DE TECLADO

```
Ninguno configurado aún
```

---

## ❓ PREGUNTAS FRECUENTES

### ¿Cómo cambio entre vista Cards y Tabla?
Click en los botones en la parte superior derecha. Tu preferencia se guarda automáticamente.

### ¿Los filtros afectan la exportación?
Sí, solo se exportan los vehículos que cumplen con los filtros aplicados.

### ¿Puedo importar vehículos duplicados?
Si la placa ya existe, el vehículo se actualiza con los nuevos datos.

### ¿Qué formato debe tener el Excel para importar?
Descarga la plantilla desde el modal de importación. Tiene el formato correcto.

### ¿El QR code tiene fecha de vencimiento?
No, el QR es permanente y contiene la información actual del vehículo.

### ¿Puedo ver el historial de cualquier vehículo?
Sí, desde el detalle de cada vehículo hay un botón "Historial".

---

## 🚨 SOLUCIÓN DE PROBLEMAS

### No puedo exportar a Excel
- Verificar que openpyxl está instalado: `pip install openpyxl`

### No puedo exportar a PDF
- Verificar que reportlab está instalado: `pip install reportlab`

### No puedo generar QR
- Verificar que qrcode está instalado: `pip install qrcode[pil]`

### Error al importar Excel
- Verificar que el formato sea correcto
- Descargar la plantilla y usarla como base
- Revisar que los estados sean válidos

### No veo el botón de Importar
- Verificar que tienes permisos de agregar vehículos
- Contactar al administrador

---

## 📞 SOPORTE

**Ejecutar verificación:**
```bash
python test_advanced_features.py
```

**Instalar dependencias:**
```bash
pip install openpyxl reportlab qrcode[pil]
```

**Iniciar servidor:**
```bash
python manage.py runserver
```

---

## 🎓 TUTORIALES PASO A PASO

### Tutorial 1: Exportar Reporte de Vehículos Activos
1. Ir a `/vehicles/`
2. En filtro "Estado" seleccionar "Activo"
3. Click en "Filtrar"
4. Click en "Exportar" → "Exportar a Excel"
5. Abrir archivo descargado

### Tutorial 2: Importar 10 Vehículos Nuevos
1. Click en "Importar"
2. Click en "Descargar Plantilla Excel"
3. Abrir plantilla en Excel
4. Llenar 10 filas con datos de vehículos
5. Guardar archivo
6. Subir archivo en el modal
7. Esperar confirmación

### Tutorial 3: Generar QR para Toda la Flotilla
1. Ir a lista de vehículos
2. Para cada vehículo:
   - Entrar al detalle
   - Click en "QR Code"
   - Guardar imagen
3. Imprimir todas las imágenes
4. Pegar en cada vehículo

---

## ✅ CHECKLIST DE USO DIARIO

- [ ] Revisar vehículos en mantenimiento
- [ ] Verificar documentos próximos a vencer
- [ ] Actualizar estados de vehículos
- [ ] Exportar reporte semanal
- [ ] Revisar historial de incidencias

---

**Última actualización:** Enero 2025  
**Versión:** 2.0 (Módulo Avanzado)  
**Sistema:** SIM - ICASA
