# ===== CREADOR DE IMÁGENES PARA EL JUEGO =====
# Este programa crea las imágenes que necesitamos para nuestro juego.
# Es como dibujar con la computadora los personajes y el fondo.

import pygame  # Esta librería nos permite dibujar cosas
import os      # Esta nos ayuda a crear carpetas y guardar archivos
import random  # Esta nos permite generar números al azar

# Primero necesitamos "encender" pygame, como cuando enciendes un lápiz mágico
print("🚀 Iniciando el creador de imágenes...")
pygame.init()

# Estos son los colores que vamos a usar, como elegir crayones de una caja
print("🎨 Preparando los colores...")
BLACK = (0, 0, 0)         # Negro (como el espacio)
WHITE = (255, 255, 255)   # Blanco (como las estrellas)
BLUE = (0, 0, 255)        # Azul (para los láseres)
LIGHT_BLUE = (135, 206, 250)  # Azul celeste (como nuestra nave actual)
PURPLE = (138, 43, 226)   # Morado/Púrpura (como nuestros alienígenas actuales)
PINK = (251, 1, 232)      # Rosa Magenta Brillante (para nave alternativa)

# Nos aseguramos de que exista una carpeta para guardar los dibujos
print("📁 Revisando si existe la carpeta para guardar los dibujos...")
if not os.path.exists("imagenes"):
    print("   ¡No existe! Vamos a crearla...")
    os.makedirs("imagenes")
else:
    print("   ¡La carpeta ya existe! Usaremos esa.")

# Vamos a crear la imagen de nuestra nave espacial
print("🚀 Dibujando tu nave espacial (triángulo azul celeste)...")
nave = pygame.Surface((50, 50), pygame.SRCALPHA)  # Como una hoja de papel transparente
pygame.draw.polygon(nave, LIGHT_BLUE, [(25, 0), (0, 50), (50, 50)])  # Dibujamos un triángulo
pygame.image.save(nave, "imagenes/nave.png")  # Guardamos el dibujo
print("   ¡Nave espacial guardada correctamente!")

# Ahora dibujamos a los alienígenas
print("👾 Dibujando los alienígenas (círculos morados)...")
alien = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(alien, PURPLE, (20, 20), 20)  # Dibujamos un círculo
pygame.image.save(alien, "imagenes/alien.png")
print("   ¡Alienígenas guardados correctamente!")

# Ahora dibujamos los rayos láser
print("💥 Dibujando los rayos láser (rectángulos azules)...")
laser = pygame.Surface((5, 20), pygame.SRCALPHA)
pygame.draw.rect(laser, BLUE, (0, 0, 5, 20))  # Dibujamos un rectángulo
pygame.image.save(laser, "imagenes/laser.png")
print("   ¡Rayos láser guardados correctamente!")

# Finalmente, dibujamos el fondo del espacio
print("🌌 Dibujando el fondo del espacio (negro con estrellas)...")
fondo = pygame.Surface((800, 600))
fondo.fill(BLACK)  # Pintamos todo de negro

# Añadimos estrellas al fondo del espacio
print("✨ Añadiendo estrellas al espacio...")
for i in range(100):  # Vamos a dibujar 100 estrellas
    x = random.randint(0, 800)  # Posición X al azar
    y = random.randint(0, 600)  # Posición Y al azar
    pygame.draw.circle(fondo, WHITE, (x, y), 1)  # Dibujamos una estrella (punto pequeño)
    if i % 25 == 0:  # Mostramos progreso cada 25 estrellas
        print(f"   {i} estrellas dibujadas...")

pygame.image.save(fondo, "imagenes/fondo.png")
print("   ¡Fondo espacial guardado correctamente!")

print("✅ ¡Todas las imágenes fueron creadas correctamente en la carpeta 'imagenes'!")
print("   Ahora el juego podrá usar estas imágenes para que puedas jugar.")
print("   ¡Prepárate para la aventura espacial! 🚀👾") 