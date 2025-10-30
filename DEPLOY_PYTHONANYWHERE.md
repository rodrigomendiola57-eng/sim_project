# 🚀 Guía para Actualizar PythonAnywhere

## Paso 1: Subir archivos a PythonAnywhere

### Opción A - Usando Git (Recomendado)

Si tienes tu proyecto en GitHub/GitLab:

1. **En tu computadora local:**
```bash
git add .
git commit -m "Actualizar colores ICASA y logo"
git push origin main
```

2. **En PythonAnywhere (consola Bash):**
```bash
cd ~/rodrigomendiola.pythonanywhere.com
git pull origin main
```

### Opción B - Subir archivos manualmente

1. Ve a PythonAnywhere → Files
2. Navega a tu proyecto
3. Sube estos archivos:
   - `static/css/main.css`
   - `static/images/ICASA.jpg`
   - `vehicles/templates/vehicles/base.html`
   - `vehicles/templates/vehicles/includes/navbar.html`

## Paso 2: Recolectar archivos estáticos en PythonAnywhere

**En la consola Bash de PythonAnywhere:**

```bash
cd ~/rodrigomendiola.pythonanywhere.com
python manage.py collectstatic --noinput --clear
```

## Paso 3: Recargar la aplicación web

1. Ve a la pestaña **Web** en PythonAnywhere
2. Click en el botón verde **"Reload rodrigomendiola.pythonanywhere.com"**
3. Espera unos segundos

## Paso 4: Limpiar caché del navegador

1. Abre https://rodrigomendiola.pythonanywhere.com/
2. Presiona **Ctrl + Shift + R** (o **Ctrl + F5**)
3. Si no funciona, limpia el caché completo del navegador

## ✅ Verificación

Deberías ver:
- ✅ Colores verdes ICASA (#3BAA35 y #006837)
- ✅ Logo ICASA en el navbar
- ✅ Navbar blanco con borde verde
- ✅ Tablas con headers verdes
- ✅ Botones verdes corporativos

## 🔧 Solución de problemas

Si aún no ves los cambios:

1. **Verifica que los archivos se subieron correctamente:**
```bash
ls -la ~/rodrigomendiola.pythonanywhere.com/static/css/
ls -la ~/rodrigomendiola.pythonanywhere.com/static/images/
```

2. **Verifica los archivos estáticos recolectados:**
```bash
ls -la ~/rodrigomendiola.pythonanywhere.com/staticfiles/css/
ls -la ~/rodrigomendiola.pythonanywhere.com/staticfiles/images/
```

3. **Elimina archivos CSS duplicados:**
```bash
rm -f ~/rodrigomendiola.pythonanywhere.com/vehicles/static/css/main.css
```

4. **Vuelve a recolectar estáticos:**
```bash
python manage.py collectstatic --noinput --clear
```

5. **Recarga la aplicación web** desde el panel de PythonAnywhere

## 📝 Comandos rápidos para copiar y pegar

```bash
# Ir al directorio del proyecto
cd ~/rodrigomendiola.pythonanywhere.com

# Si usas Git
git pull origin main

# Eliminar CSS duplicado
rm -f vehicles/static/css/main.css

# Recolectar estáticos
python manage.py collectstatic --noinput --clear

# Luego ve al panel Web y haz click en "Reload"
```
