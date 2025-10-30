from PIL import Image
import collections

# Abrir la imagen
img = Image.open(r'C:\sim_project\static\images\icasa logo verde.jpg')
img = img.convert('RGB')

# Obtener todos los píxeles
pixels = list(img.getdata())

# Filtrar solo píxeles verdes (donde G > R y G > B)
green_pixels = [p for p in pixels if p[1] > p[0] and p[1] > p[2] and p[1] > 100]

if green_pixels:
    # Encontrar el color verde más común
    most_common = collections.Counter(green_pixels).most_common(5)
    
    print("Los 5 tonos de verde más comunes en el logo:")
    print("-" * 50)
    for i, (color, count) in enumerate(most_common, 1):
        r, g, b = color
        hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
        print(f"{i}. RGB({r}, {g}, {b}) = {hex_color}")
        print(f"   Aparece {count} veces")
        print()
else:
    print("No se encontraron píxeles verdes dominantes")
