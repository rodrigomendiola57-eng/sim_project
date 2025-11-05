# 🚗 Módulo de Vehículos - Funcionalidades Avanzadas

## ✅ Funcionalidades Implementadas

### 📤 1. Exportar a Excel
**Ubicación:** Lista de Vehículos → Botón "Exportar" → "Exportar a Excel"

**Características:**
- Exporta todos los vehículos filtrados a formato Excel (.xlsx)
- Respeta los filtros aplicados (búsqueda, estación, estado, año)
- Incluye columnas: Placa, Marca, Modelo, Año, Estado, Estación, Fecha Registro
- Formato profesional con colores corporativos ICASA (#80AD46)
- Ajuste automático de anchos de columna
- Nombre de archivo con timestamp: `vehiculos_YYYYMMDD_HHMMSS.xlsx`

**URL:** `/vehicles/export/excel/`

---

### 📄 2. Exportar a PDF
**Ubicación:** Lista de Vehículos → Botón "Exportar" → "Exportar a PDF"

**Características:**
- Genera reporte PDF profesional con todos los vehículos filtrados
- Respeta los filtros aplicados
- Incluye título con colores corporativos
- Fecha y hora de generación
- Tabla con bordes y formato profesional
- Nombre de archivo con timestamp: `vehiculos_YYYYMMDD_HHMMSS.pdf`

**URL:** `/vehicles/export/pdf/`

---

### 📥 3. Importar desde Excel
**Ubicación:** Lista de Vehículos → Botón "Importar"

**Características:**
- Modal con drag & drop para subir archivo Excel
- Descarga de plantilla Excel con formato correcto
- Validación de datos antes de importar
- Crea nuevos vehículos o actualiza existentes (por placa)
- Reporte detallado: cantidad creados, actualizados y errores
- Formato requerido: Placa, Marca, Modelo, Año, Estado, Estación

**URLs:**
- Importar: `/vehicles/import/excel/` (POST)
- Descargar plantilla: `/vehicles/template/download/`

**Formato de Excel:**
```
| Placa   | Marca  | Modelo | Año  | Estado | Estación          |
|---------|--------|--------|------|--------|-------------------|
| ABC-123 | Toyota | Hilux  | 2023 | Active | Ciudad de México  |
| XYZ-789 | Ford   | Ranger | 2022 | Active | Jalisco           |
```

---

### 📈 4. Historial del Vehículo (Timeline)
**Ubicación:** Detalle del Vehículo → Botón "Historial"

**Características:**
- Timeline visual con todos los eventos del vehículo
- Muestra mantenimientos y documentos en orden cronológico
- Iconos diferenciados por tipo de evento
- Colores por estado (Detectado, Cotizado, Aprobado, Completado, etc.)
- Información detallada de cada evento:
  - **Mantenimientos:** Estado, costo, taller, descripción
  - **Documentos:** Estado (vigente/expirado), fecha de vencimiento, número
- Línea de tiempo vertical con badges de colores
- Diseño responsive y moderno

**URL:** `/vehicles/<id>/history/`

---

### 🔗 5. Código QR por Vehículo
**Ubicación:** Detalle del Vehículo → Botón "QR Code"

**Características:**
- Genera código QR único por vehículo
- Información incluida en el QR:
  - Placa
  - Marca y Modelo
  - Año
  - Estado actual
  - Estación asignada
- Color corporativo ICASA (#80AD46)
- Descarga automática como imagen PNG
- Nombre de archivo: `qr_PLACA.png`
- Útil para etiquetas físicas en vehículos

**URL:** `/vehicles/<id>/qr/`

---

## 🎨 Mejoras Visuales Implementadas

### Lista de Vehículos
- ✅ Vista toggle Cards/Tabla (guardado en localStorage)
- ✅ Cards modernos con hover effects
- ✅ Badges con gradientes para estados
- ✅ Filtros avanzados (búsqueda, estación, estado, año)
- ✅ Botones de exportar/importar en header
- ✅ Hero section con gradiente ICASA
- ✅ Paginación de 50 elementos

### Detalle del Vehículo
- ✅ Botones de Historial y QR Code
- ✅ Layout mejorado con cards
- ✅ Información organizada en secciones

### Historial del Vehículo
- ✅ Timeline vertical con líneas conectoras
- ✅ Badges de colores por tipo de evento
- ✅ Cards con borde lateral de color
- ✅ Información del vehículo en header
- ✅ Iconos FontAwesome para cada tipo de evento

---

## 📦 Dependencias Instaladas

```txt
openpyxl>=3.1.2      # Para Excel
reportlab>=4.0.0     # Para PDF
qrcode>=7.4.2        # Para QR codes
```

---

## 🔧 Archivos Creados/Modificados

### Nuevos Archivos
- `vehicles/views_vehicle_advanced.py` - Vistas avanzadas
- `vehicles/templates/vehicles/vehicle_history.html` - Template historial
- `MODULO_VEHICULOS_AVANZADO.md` - Esta documentación

### Archivos Modificados
- `vehicles/urls.py` - URLs nuevas
- `vehicles/templates/vehicles/vehicle_list_new.html` - Botones exportar/importar
- `vehicles/templates/vehicles/vehicle_detail.html` - Botones historial/QR
- `requirements.txt` - Dependencias

---

## 🚀 Cómo Usar

### Exportar Vehículos
1. Ir a lista de vehículos
2. Aplicar filtros deseados (opcional)
3. Click en "Exportar" → Elegir Excel o PDF
4. El archivo se descarga automáticamente

### Importar Vehículos
1. Click en "Importar"
2. Descargar plantilla Excel (opcional)
3. Llenar Excel con datos de vehículos
4. Subir archivo en el modal
5. Ver reporte de importación

### Ver Historial
1. Entrar al detalle de un vehículo
2. Click en "Historial"
3. Ver timeline completo de eventos

### Generar QR
1. Entrar al detalle de un vehículo
2. Click en "QR Code"
3. La imagen PNG se descarga automáticamente
4. Imprimir y pegar en el vehículo

---

## 🎯 Próximas Mejoras Sugeridas

- [ ] Exportar historial individual a PDF
- [ ] Gráficos de costos de mantenimiento por vehículo
- [ ] Alertas de documentos próximos a vencer
- [ ] Comparativa de costos entre vehículos
- [ ] Dashboard de estadísticas por vehículo
- [ ] Integración con GPS para tracking

---

## 📊 Estadísticas del Módulo

- **Vistas creadas:** 6 nuevas vistas
- **Templates creados:** 1 nuevo template
- **URLs agregadas:** 5 nuevas rutas
- **Funcionalidades:** 5 features completas
- **Librerías integradas:** 3 (openpyxl, reportlab, qrcode)

---

**Desarrollado para:** ICASA - Integradores de Carga Aérea  
**Sistema:** SIM - Sistema Integral de Mantenimiento  
**Fecha:** Enero 2025
