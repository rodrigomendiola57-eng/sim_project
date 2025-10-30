import os

print("📋 Instrucciones para actualizar PythonAnywhere:\n")
print("=" * 60)
print("\n1️⃣ Abre la consola Bash en PythonAnywhere")
print("\n2️⃣ Navega a tu proyecto:")
print("   cd ~/sim_project")
print("\n3️⃣ Edita el archivo CSS:")
print("   nano static/css/main.css")
print("\n4️⃣ Busca la sección '.navbar {' y reemplaza con:")
print("""
.navbar {
    background: linear-gradient(to right, #ffffff 0%, #f0fdf4 100%);
    padding: 0.75rem 0;
    border-bottom: 3px solid var(--primary-color);
    box-shadow: var(--shadow-md);
}

.navbar .container {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.navbar-collapse {
    flex-grow: 0;
}

.navbar-nav {
    gap: 0.25rem;
}
""")
print("\n5️⃣ Busca '.logo-icon {' y cambia:")
print("   width: 80px;  →  width: 60px;")
print("   height: 80px;  →  height: 60px;")
print("   border-radius: 12px;  →  border-radius: 10px;")
print("   padding: 8px;  →  padding: 6px;")
print("\n6️⃣ Busca '.nav-link {' y reemplaza con:")
print("""
.nav-link {
    font-weight: 500;
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem !important;
    border-radius: var(--radius-sm);
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 0.375rem;
    color: var(--text-secondary) !important;
    white-space: nowrap;
}
""")
print("\n7️⃣ Busca '.dropdown-menu {' y agrega al final:")
print("""
.dropdown-menu-end {
    right: 0;
    left: auto;
}
""")
print("\n8️⃣ Edita el navbar:")
print("   nano vehicles/templates/vehicles/includes/navbar.html")
print("\n9️⃣ Busca la línea con 'navbar-nav ms-auto' y cambia a:")
print('   <ul class="navbar-nav ms-auto align-items-center">')
print("\n🔟 Guarda (Ctrl+O, Enter, Ctrl+X) y ejecuta:")
print("   python manage.py collectstatic --noinput")
print("   touch /var/www/icasaoperador_pythonanywhere_com_wsgi.py")
print("\n✅ Recarga tu sitio web")
print("=" * 60)
