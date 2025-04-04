##############################################################
# 🚀 JUEGO: SPACE INVADERS PARA NIÑOS 👾
##############################################################
# ¡Hola! Este es un juego de naves espaciales donde tú serás el piloto
# y tendrás que defender la Tierra de invasores alienígenas.
# Si tienes entre 7 y 16 años, ¡este juego te ayudará a aprender
# cómo se hacen los videojuegos!
#
# CÓMO ESTÁ ORGANIZADO ESTE PROGRAMA:
# Imagina que construimos una casa. Primero necesitamos los materiales,
# luego hacemos los cimientos, las paredes, y finalmente el techo.
# Un programa se construye de forma parecida:
#
# 1. IMPORTAR LIBRERÍAS: Son como nuestras herramientas mágicas
#    que nos permiten hacer cosas especiales, como mostrar imágenes.
#
# 2. CONFIGURACIÓN INICIAL: Preparamos la ventana del juego y definimos 
#    los colores que usaremos, como elegir los lápices para dibujar.
#
# 3. CREACIÓN DE IMÁGENES: Dibujamos la nave, los alienígenas y los rayos láser.
#
# 4. CARGA DE RECURSOS: Abrimos las imágenes que usaremos en el juego.
#
# 5. CLASES DE OBJETOS: Es como crear un tipo especial de juguete con reglas.
#    - Clase Player: Es nuestra nave espacial que controlamos.
#    - Clase Laser: Son los rayos que dispara nuestra nave.
#    - Clase Enemy: Son los alienígenas que tenemos que derrotar.
#    - Clase Boss: Un alienígena jefe más difícil.
#    - Clase FastEnemy: Alienígenas que se mueven más rápido.
#
# 6. FUNCIÓN DE COLISIONES: Nos dice cuando un láser golpea a un alienígena.
#
# 7. FUNCIÓN DE MENÚ: Muestra las opciones al inicio del juego.
#
# 8. FUNCIÓN PRINCIPAL: ¡Aquí es donde ocurre toda la acción del juego!
#
# 9. FUNCIÓN MODO DESAFÍO: Un modo especial más difícil con jefes.
#
# 10. INICIO DEL JUEGO: Donde empezamos a jugar.
#
# ¡Sigue leyendo si quieres aprender cómo funciona todo! 🎮
##############################################################

# ======== 1. IMPORTAR LIBRERÍAS ========
# Las librerías son como cajas de herramientas mágicas que nos ayudan a hacer el juego
import pygame  # Esta librería nos permite crear videojuegos, dibujar y mostrar cosas en la pantalla
import sys     # Esta nos ayuda a cerrar el juego correctamente cuando queremos salir
import random  # Esta nos permite crear números al azar, como lanzar un dado
import os      # Esta nos ayuda a trabajar con archivos y carpetas en el ordenador

# ======== 2. CONFIGURACIÓN INICIAL ========
# ¡Preparamos todo para que nuestro juego funcione!
pygame.init()  # Esta línea es como "encender" pygame para poder usarlo

# Configuramos el tamaño de la ventana del juego
WIDTH, HEIGHT = 800, 600  # Ancho y alto de la pantalla en píxeles (puntos de la pantalla)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Creamos la ventana del juego
pygame.display.set_caption("Space Invaders para Niños")  # Ponemos un título a la ventana

# Definimos los colores que usaremos en el juego
# Los colores se forman mezclando Rojo, Verde y Azul (RGB)
# Cada color puede tener un valor de 0 a 255
BLACK = (0, 0, 0)         # Negro (como el espacio): sin nada de rojo, verde ni azul
WHITE = (255, 255, 255)   # Blanco (como las estrellas): máximo rojo, verde y azul
GREEN = (0, 255, 0)       # Verde brillante: máximo verde, sin rojo ni azul
RED = (255, 0, 0)         # Rojo brillante: máximo rojo, sin verde ni azul
BLUE = (0, 0, 255)        # Azul brillante: máximo azul, sin rojo ni verde
LIGHT_BLUE = (135, 206, 250)  # Azul celeste: mezcla de un poco de rojo, bastante verde y mucho azul
PURPLE = (138, 43, 226)   # Púrpura/Morado: mezcla de rojo y azul, poco verde
YELLOW = (255, 255, 0)    # Amarillo brillante: máximo rojo y verde, sin azul
ORANGE = (255, 165, 0)    # Naranja: máximo rojo, bastante verde, sin azul
PINK = (251, 1, 232)      # Rosa Magenta Brillante: mucho rojo, casi nada de verde, bastante azul
CYAN = (0, 255, 255)      # Cian (azul verdoso): máximo verde y azul, sin rojo
LIME = (50, 205, 50)      # Verde Lima: un poco de rojo, mucho verde, poco azul
MENU_BG = (25, 25, 50)    # Azul oscuro (para el fondo del menú)
BUTTON_COLOR = (75, 75, 200)  # Azul para botones
BUTTON_HOVER = (100, 100, 255)  # Azul más claro para cuando pasamos el ratón sobre botones

# Variables para controlar el menú del juego
menu_active = True      # Esta variable nos dice si estamos en el menú o no
game_mode = "normal"    # El modo de juego que elegimos (normal o desafío)
selected_option = 0     # La opción que tenemos seleccionada en el menú

# Variables para las opciones personalizables
nave_color = LIGHT_BLUE  # El color que tendrá nuestra nave (podemos cambiarlo)
enemy_speed_multiplier = 1.0  # Qué tan rápido se moverán los enemigos (1.0 es velocidad normal)

# ======== 3. CREACIÓN DE IMÁGENES ========
# Esta función es como tener un cuaderno de dibujo donde creamos los personajes del juego
def create_images():
    # Primero nos aseguramos de tener una carpeta para guardar nuestros dibujos
    if not os.path.exists("imagenes"):
        os.makedirs("imagenes")  # Si no existe la carpeta, la creamos
    
    # Dibujamos nuestra nave espacial (un triángulo azul celeste)
    print("🚀 Dibujando tu nave espacial...")
    nave = pygame.Surface((50, 50), pygame.SRCALPHA)  # Un lienzo transparente de 50x50 píxeles
    pygame.draw.polygon(nave, LIGHT_BLUE, [(25, 0), (0, 50), (50, 50)])  # Dibujamos un triángulo
    pygame.image.save(nave, "imagenes/nave.png")  # Guardamos el dibujo como imagen
    
    # Dibujamos a los alienígenas (círculos morados)
    print("👾 Dibujando a los alienígenas...")
    alien = pygame.Surface((40, 40), pygame.SRCALPHA)  # Un lienzo transparente de 40x40 píxeles
    pygame.draw.circle(alien, PURPLE, (20, 20), 20)  # Dibujamos un círculo
    pygame.image.save(alien, "imagenes/alien.png")  # Guardamos el dibujo como imagen
    
    # Dibujamos los rayos láser (rectángulos azules)
    print("💥 Dibujando los rayos láser...")
    laser = pygame.Surface((5, 20), pygame.SRCALPHA)  # Un lienzo transparente delgado
    pygame.draw.rect(laser, BLUE, (0, 0, 5, 20))  # Dibujamos un rectángulo
    pygame.image.save(laser, "imagenes/laser.png")  # Guardamos el dibujo como imagen
    
    # Dibujamos el fondo del espacio (negro con estrellas)
    print("🌌 Creando el espacio exterior...")
    fondo = pygame.Surface((800, 600))  # Un lienzo del tamaño de nuestra ventana
    fondo.fill(BLACK)  # Pintamos todo de negro como el espacio
    
    # Añadimos estrellas (pequeños puntos blancos) por todo el espacio
    print("✨ Añadiendo estrellas al espacio...")
    for _ in range(100):  # Vamos a añadir 100 estrellas
        x = random.randint(0, 800)  # Posición X al azar (horizontal)
        y = random.randint(0, 600)  # Posición Y al azar (vertical)
        pygame.draw.circle(fondo, WHITE, (x, y), 1)  # Dibujamos una estrella pequeñita
    
    pygame.image.save(fondo, "imagenes/fondo.png")  # Guardamos el dibujo como imagen
    
    print("✅ ¡Todas las imágenes se han creado correctamente!")

# ======== 4. CARGA DE RECURSOS ========
# Comprobamos si ya tenemos las imágenes y si no, las creamos
print("🔍 Buscando las imágenes para el juego...")
if not os.path.exists("imagenes/nave.png") or \
   not os.path.exists("imagenes/alien.png") or \
   not os.path.exists("imagenes/laser.png") or \
   not os.path.exists("imagenes/fondo.png"):
    print("🖌️ No encontramos todas las imágenes, vamos a crearlas...")
    create_images()
else:
    print("📁 ¡Encontramos todas las imágenes! Las usaremos para el juego.")

# Cargamos las imágenes para usarlas en el juego
try:
    print("📥 Cargando las imágenes en el juego...")
    player_img = pygame.image.load('imagenes/nave.png')  # Cargamos la imagen de la nave
    enemy_img = pygame.image.load('imagenes/alien.png')  # Cargamos la imagen del alien
    laser_img = pygame.image.load('imagenes/laser.png')  # Cargamos la imagen del láser
    background_img = pygame.image.load('imagenes/fondo.png')  # Cargamos la imagen del fondo
    
    # Ajustamos el tamaño de las imágenes para que se vean bien en el juego
    player_img = pygame.transform.scale(player_img, (50, 50))  # Tamaño de la nave
    enemy_img = pygame.transform.scale(enemy_img, (40, 40))  # Tamaño del alien
    laser_img = pygame.transform.scale(laser_img, (5, 20))  # Tamaño del láser
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Tamaño del fondo
    print("✅ ¡Imágenes cargadas correctamente!")
except pygame.error as e:
    # Si hay algún problema al cargar las imágenes, usaremos figuras geométricas
    print(f"❌ Hubo un problema al cargar las imágenes: {e}")
    print("🔶 Usaremos figuras geométricas en su lugar.")
    player_img = None  # No hay imagen de nave
    enemy_img = None   # No hay imagen de alien
    laser_img = None   # No hay imagen de láser
    background_img = None  # No hay imagen de fondo

# ======== 5. CLASES DE OBJETOS ========
# Las clases son como "moldes" para crear objetos en el juego.
# Es como si tuvieras un molde para hacer galletas: cada galleta
# tendrá la misma forma, pero pueden tener diferentes sabores o decoraciones.

# Clase del jugador (nuestra nave espacial)
class Player:
    def __init__(self, color=nave_color):
        # Esto se ejecuta cuando creamos una nueva nave
        self.x = WIDTH // 2  # Posición X (en medio de la pantalla)
        self.y = HEIGHT - 70  # Posición Y (cerca del fondo)
        self.speed = 5  # Qué tan rápido se mueve nuestra nave
        self.width = 50  # Ancho de la nave
        self.height = 50  # Alto de la nave
        self.lasers = []  # Lista para guardar los láseres que disparemos
        self.color = color  # Color de la nave (podemos cambiarlo)
    
    def draw(self):
        # Esta función dibuja nuestra nave en la pantalla
        if player_img:  # Si tenemos una imagen de nave
            # Creamos una copia de la imagen y la pintamos del color elegido
            colored_ship = player_img.copy()
            # Creamos una capa del color seleccionado
            color_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            color_surface.fill(self.color)
            # Mezclamos la imagen original con el color elegido
            colored_ship.blit(color_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            # Mostramos la nave en su posición
            screen.blit(colored_ship, (self.x, self.y))
        else:  # Si no tenemos imagen, dibujamos un rectángulo
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def move(self, direction):
        # Esta función mueve nuestra nave a la izquierda o derecha
        if direction == "left" and self.x > 0:  # Si vamos a la izquierda y no nos salimos
            self.x -= self.speed  # Movemos a la izquierda
        if direction == "right" and self.x < WIDTH - self.width:  # Si vamos a la derecha y no nos salimos
            self.x += self.speed  # Movemos a la derecha
    
    def shoot(self):
        # Esta función hace que nuestra nave dispare un láser
        # Creamos un láser en la posición de la nave (en el centro y arriba)
        laser = Laser(self.x + self.width // 2 - 2, self.y)
        self.lasers.append(laser)  # Lo añadimos a la lista de láseres
    
    def update_lasers(self):
        # Esta función actualiza todos los láseres que hemos disparado
        for laser in self.lasers[:]:  # Para cada láser en la lista
            laser.move()  # Movemos el láser
            if laser.y < 0:  # Si el láser se sale de la pantalla por arriba
                self.lasers.remove(laser)  # Lo quitamos de la lista

# Clase del láser (los rayos que dispara nuestra nave)
class Laser:
    def __init__(self, x, y):
        # Esto se ejecuta cuando creamos un nuevo láser
        self.x = x  # Posición X (horizontal)
        self.y = y  # Posición Y (vertical)
        self.speed = 7  # Qué tan rápido sube el láser (más rápido que la nave)
        self.width = 5  # Ancho del láser
        self.height = 20  # Alto del láser
    
    def draw(self):
        # Esta función dibuja el láser en la pantalla
        if laser_img:  # Si tenemos una imagen de láser
            screen.blit(laser_img, (self.x, self.y))  # Mostramos la imagen
        else:  # Si no tenemos imagen, dibujamos un rectángulo azul
            pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
    
    def move(self):
        # Esta función mueve el láser hacia arriba
        self.y -= self.speed  # Restamos a Y para que suba (en pantallas Y=0 es arriba)

# Clase del enemigo (los alienígenas que queremos derrotar)
class Enemy:
    def __init__(self, x, y, speed_multiplier=enemy_speed_multiplier):
        # Esto se ejecuta cuando creamos un nuevo alienígena
        self.x = x  # Posición X (horizontal)
        self.y = y  # Posición Y (vertical)
        self.base_speed = 1  # Velocidad base (qué tan rápido se mueve normalmente)
        self.speed = self.base_speed * speed_multiplier  # Velocidad actual, puede aumentar
        self.width = 40  # Ancho del alienígena
        self.height = 40  # Alto del alienígena
        self.direction = 1  # Dirección: 1 es derecha, -1 es izquierda
    
    def draw(self):
        # Esta función dibuja el alienígena en la pantalla
        if enemy_img:  # Si tenemos una imagen de alienígena
            screen.blit(enemy_img, (self.x, self.y))  # Mostramos la imagen
        else:  # Si no tenemos imagen, dibujamos un círculo morado
            pygame.draw.rect(screen, PURPLE, (self.x, self.y, self.width, self.height))
    
    def move(self):
        # Esta función mueve al alienígena de lado a lado
        self.x += self.speed * self.direction  # Movemos según velocidad y dirección
        
        # Si el alienígena llega al borde de la pantalla, cambia de dirección y baja un poco
        if self.x <= 0:  # Si llega al borde izquierdo
            self.x = 0  # Lo mantenemos en el borde
            self.direction = 1  # Cambiamos dirección hacia la derecha
            self.y += 20  # Bajamos un poco
        elif self.x + self.width >= WIDTH:  # Si llega al borde derecho
            self.x = WIDTH - self.width  # Lo mantenemos en el borde
            self.direction = -1  # Cambiamos dirección hacia la izquierda
            self.y += 20  # Bajamos un poco

# Clase de enemigo rápido (alienígenas que se mueven más rápido)
class FastEnemy:
    def __init__(self, x, y, speed_multiplier=enemy_speed_multiplier):
        # Esto se ejecuta cuando creamos un nuevo alienígena rápido
        self.x = x  # Posición X (horizontal)
        self.y = y  # Posición Y (vertical)
        self.base_speed = 2  # Velocidad base (el doble que un enemigo normal)
        self.speed = self.base_speed * speed_multiplier  # Velocidad actual, puede aumentar
        self.width = 30  # Un poco más pequeño que un enemigo normal
        self.height = 30  # Un poco más pequeño que un enemigo normal
        self.direction = 1  # Dirección: 1 es derecha, -1 es izquierda
    
    def draw(self):
        # Esta función dibuja el alienígena rápido (naranja con líneas rojas)
        pygame.draw.rect(screen, ORANGE, (self.x, self.y, self.width, self.height))
        # Añadimos líneas rojas en X para que parezca peligroso
        pygame.draw.line(screen, RED, (self.x, self.y), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, RED, (self.x + self.width, self.y), (self.x, self.y + self.height), 2)
    
    def move(self):
        # Esta función mueve al alienígena rápido (puede cambiar de dirección al azar)
        self.x += self.speed * self.direction  # Movemos según velocidad y dirección
        
        # A veces cambia de dirección aleatoriamente (para dar sorpresas)
        if random.randint(1, 100) == 1:  # 1% de probabilidad en cada actualización
            self.direction *= -1  # Multiplicar por -1 invierte la dirección
        
        # Si el alienígena llega al borde de la pantalla, cambia de dirección
        if self.x <= 0:  # Si llega al borde izquierdo
            self.x = 0  # Lo mantenemos en el borde
            self.direction = 1  # Cambiamos dirección hacia la derecha
        elif self.x + self.width >= WIDTH:  # Si llega al borde derecho
            self.x = WIDTH - self.width  # Lo mantenemos en el borde
            self.direction = -1  # Cambiamos dirección hacia la izquierda

# Clase del jefe alienígena (un enemigo más grande y resistente)
class Boss:
    def __init__(self, x, y, speed_multiplier=enemy_speed_multiplier):
        # Esto se ejecuta cuando creamos un nuevo jefe alienígena
        self.x = x  # Posición X (horizontal)
        self.y = y  # Posición Y (vertical)
        self.base_speed = 1.5  # Velocidad base (más rápido que un enemigo normal)
        self.speed = self.base_speed * speed_multiplier  # Velocidad actual, puede aumentar
        self.width = 80  # El doble de grande que un enemigo normal
        self.height = 80  # El doble de grande que un enemigo normal
        self.direction = 1  # Dirección: 1 es derecha, -1 es izquierda
        self.health = 5  # Vida del jefe (necesita 5 disparos para ser derrotado)
    
    def draw(self):
        # Esta función dibuja el jefe alienígena (amarillo con ojos y boca rojos)
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.width, self.height))
        
        # Añadimos detalles para que parezca un jefe alienígena asustador
        # Ojos rojos
        pygame.draw.circle(screen, RED, (int(self.x + self.width//4), int(self.y + self.height//3)), 10)
        pygame.draw.circle(screen, RED, (int(self.x + 3*self.width//4), int(self.y + self.height//3)), 10)
        
        # Boca roja
        pygame.draw.arc(screen, RED, 
                      (self.x + self.width//4, self.y + self.height//2, self.width//2, self.height//3),
                      0.2, 2.9, 3)
        
        # Barra de vida (se hace más pequeña cuando recibe daño)
        health_width = (self.width * self.health) // 5  # Ancho proporcional a la vida
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, health_width, 5))
    
    def move(self):
        # Esta función mueve al jefe alienígena
        self.x += self.speed * self.direction  # Movemos según velocidad y dirección
        
        # Si el jefe llega al borde de la pantalla, cambia de dirección
        if self.x <= 0:  # Si llega al borde izquierdo
            self.x = 0  # Lo mantenemos en el borde
            self.direction = 1  # Cambiamos dirección hacia la derecha
        elif self.x + self.width >= WIDTH:  # Si llega al borde derecho
            self.x = WIDTH - self.width  # Lo mantenemos en el borde
            self.direction = -1  # Cambiamos dirección hacia la izquierda

# ======== 6. FUNCIÓN DE COLISIONES ========
# Esta función comprueba si un láser ha golpeado a un alienígena
def check_collision(laser, enemy):
    # Las colisiones ocurren cuando dos objetos se tocan o se superponen
    # Comprobamos si el láser está tocando al enemigo usando sus coordenadas
    # Para que haya una colisión, el láser y el enemigo deben coincidir en el espacio
    if (laser.x < enemy.x + enemy.width and  # El láser está a la izquierda del borde derecho del enemigo
        laser.x + laser.width > enemy.x and  # El láser está a la derecha del borde izquierdo del enemigo
        laser.y < enemy.y + enemy.height and  # El láser está arriba del borde inferior del enemigo
        laser.y + laser.height > enemy.y):   # El láser está debajo del borde superior del enemigo
        return True  # ¡Hay colisión! El láser ha golpeado al enemigo
    return False  # No hay colisión, el láser no ha golpeado al enemigo

# ======== 7. FUNCIÓN DE MENÚ ========
# Esta función muestra el menú principal donde elegimos cómo queremos jugar
def show_menu():
    # Preparamos las letras para el menú
    title_font = pygame.font.SysFont(None, 80)  # Letra grande para el título
    menu_font = pygame.font.SysFont(None, 50)   # Letra mediana para las opciones
    
    # Lista de opciones que podemos elegir
    menu_options = ["Modo Normal", "Modo Desafío", "Opciones", "Salir"]
    
    # Opción que tenemos seleccionada (empezamos con la primera)
    selected = 0
    
    # Bucle del menú (sigue mostrándose hasta que elijamos una opción)
    while True:
        # Miramos qué teclas está presionando el jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si cierra la ventana
                pygame.quit()  # Cerramos pygame
                sys.exit()  # Salimos del programa
            
            if event.type == pygame.KEYDOWN:  # Si presiona una tecla
                if event.key == pygame.K_UP:  # Si es la flecha arriba
                    # Movemos la selección hacia arriba (si estamos en la primera, vamos a la última)
                    selected = (selected - 1) % len(menu_options)
                
                if event.key == pygame.K_DOWN:  # Si es la flecha abajo
                    # Movemos la selección hacia abajo (si estamos en la última, vamos a la primera)
                    selected = (selected + 1) % len(menu_options)
                
                if event.key == pygame.K_RETURN:  # Si presiona Enter (para seleccionar)
                    if selected == 0:  # Modo Normal
                        return "normal"  # Elegimos el modo normal y salimos del menú
                    elif selected == 1:  # Modo Desafío
                        return "desafio"  # Elegimos el modo desafío y salimos del menú
                    elif selected == 2:  # Opciones
                        show_options()  # Mostramos la pantalla de opciones
                    elif selected == 3:  # Salir
                        pygame.quit()  # Cerramos pygame
                        sys.exit()  # Salimos del programa
        
        # Pintamos el fondo del menú
        screen.fill(MENU_BG)
        
        # Si tenemos imagen de fondo, la usamos con un efecto semitransparente
        if background_img:
            # Hacemos una copia de la imagen y la oscurecemos para el menú
            menu_bg = background_img.copy()
            dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            dark_surface.fill((0, 0, 0, 150))  # Negro semitransparente
            menu_bg.blit(dark_surface, (0, 0))
            screen.blit(menu_bg, (0, 0))
        
        # Dibujamos el título del juego
        title_text = title_font.render("SPACE INVADERS", True, WHITE)
        title_subtitle = menu_font.render("Para Niños", True, LIGHT_BLUE)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 100))
        screen.blit(title_subtitle, (WIDTH//2 - title_subtitle.get_width()//2, 170))
        
        # Dibujamos estrellas decorativas alrededor del título
        for _ in range(20):
            star_x = random.randint(WIDTH//2 - 200, WIDTH//2 + 200)
            star_y = random.randint(80, 200)
            star_size = random.randint(1, 3)
            pygame.draw.circle(screen, WHITE, (star_x, star_y), star_size)
        
        # Dibujamos cada opción del menú
        for i, option in enumerate(menu_options):
            # Si esta opción está seleccionada, la pintamos amarilla, si no, blanca
            if i == selected:
                color = YELLOW  # Opción seleccionada
                # Dibujamos un cohete como cursor para señalar la opción seleccionada
                pygame.draw.polygon(screen, LIGHT_BLUE, [
                    (WIDTH//2 - 160, 280 + i * 70),
                    (WIDTH//2 - 180, 290 + i * 70),
                    (WIDTH//2 - 180, 310 + i * 70),
                    (WIDTH//2 - 160, 320 + i * 70)
                ])
                # Dibujamos el fuego del cohete
                pygame.draw.polygon(screen, ORANGE, [
                    (WIDTH//2 - 180, 295 + i * 70),
                    (WIDTH//2 - 190, 300 + i * 70),
                    (WIDTH//2 - 180, 305 + i * 70)
                ])
            else:
                color = WHITE  # Opciones no seleccionadas
            
            # Mostramos el texto de la opción
            option_text = menu_font.render(option, True, color)
            screen.blit(option_text, (WIDTH//2 - option_text.get_width()//2, 300 + i * 70))
        
        # Añadimos instrucciones en la parte inferior
        instructions = pygame.font.SysFont(None, 24).render(
            "Usa ↑↓ para moverte y ENTER para seleccionar", True, WHITE)
        screen.blit(instructions, (WIDTH//2 - instructions.get_width()//2, HEIGHT - 50))
        
        # Actualizamos la pantalla para que se vean los cambios
        pygame.display.update()
        
        # Controlamos la velocidad de actualización del menú
        pygame.time.Clock().tick(30)  # 30 imágenes por segundo

# ======== 7.2 FUNCIÓN DE OPCIONES ========
# Esta función muestra la pantalla donde podemos personalizar el juego
def show_options():
    # Necesitamos poder cambiar estas variables que están fuera de esta función
    global nave_color, enemy_speed_multiplier
    
    # Preparamos las letras para el menú de opciones
    title_font = pygame.font.SysFont(None, 60)  # Letra grande para el título
    option_font = pygame.font.SysFont(None, 40)  # Letra mediana para las opciones
    
    # Lista de colores entre los que podemos elegir para nuestra nave
    color_options = [
        {"name": "Azul Celeste", "color": LIGHT_BLUE},
        {"name": "Cian", "color": CYAN},
        {"name": "Verde Lima", "color": LIME},
        {"name": "Rojo", "color": RED},
        {"name": "Verde", "color": GREEN},
    ]
    
    # Buscamos cuál es el color actual de la nave en nuestra lista
    current_color_index = 0  # Empezamos asumiendo que es el primero
    for i, option in enumerate(color_options):
        if option["color"] == nave_color:  # Si encontramos el color actual
            current_color_index = i  # Guardamos su posición en la lista
            break
    
    # Lista de velocidades entre las que podemos elegir para los enemigos
    speed_options = [
        {"name": "Lento", "value": 0.5},    # Mitad de velocidad normal
        {"name": "Normal", "value": 1.0},   # Velocidad normal
        {"name": "Rápido", "value": 1.5},   # 50% más rápido que normal
        {"name": "Muy Rápido", "value": 2.0},  # Doble de velocidad normal
    ]
    
    # Buscamos cuál es la velocidad actual en nuestra lista
    current_speed_index = 1  # Por defecto es "Normal" (índice 1)
    for i, option in enumerate(speed_options):
        # Comparamos con un pequeño margen de error (por si hay decimales)
        if abs(option["value"] - enemy_speed_multiplier) < 0.1:
            current_speed_index = i  # Guardamos su posición en la lista
            break
    
    # Opción que tenemos seleccionada en el menú de opciones
    selected_option = 0  # 0: Color de Nave, 1: Velocidad de Enemigos, 2: Guardar y Volver
    
    # Bucle de la pantalla de opciones
    while True:
        # Miramos qué teclas está presionando el jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si cierra la ventana
                pygame.quit()  # Cerramos pygame
                sys.exit()  # Salimos del programa
            
            if event.type == pygame.KEYDOWN:  # Si presiona una tecla
                if event.key == pygame.K_UP:  # Si es la flecha arriba
                    # Movemos la selección hacia arriba (de 0 a 2)
                    selected_option = (selected_option - 1) % 3
                
                if event.key == pygame.K_DOWN:  # Si es la flecha abajo
                    # Movemos la selección hacia abajo (de 0 a 2)
                    selected_option = (selected_option + 1) % 3
                
                if event.key == pygame.K_LEFT:  # Si es la flecha izquierda
                    if selected_option == 0:  # Si estamos en Color de Nave
                        # Movemos a la opción anterior (o a la última si estamos en la primera)
                        current_color_index = (current_color_index - 1) % len(color_options)
                        # Cambiamos el color de la nave al seleccionado
                        nave_color = color_options[current_color_index]["color"]
                    elif selected_option == 1:  # Si estamos en Velocidad de Enemigos
                        # Movemos a la opción anterior (o a la última si estamos en la primera)
                        current_speed_index = (current_speed_index - 1) % len(speed_options)
                        # Cambiamos la velocidad de los enemigos a la seleccionada
                        enemy_speed_multiplier = speed_options[current_speed_index]["value"]
                
                if event.key == pygame.K_RIGHT:  # Si es la flecha derecha
                    if selected_option == 0:  # Si estamos en Color de Nave
                        # Movemos a la siguiente opción (o a la primera si estamos en la última)
                        current_color_index = (current_color_index + 1) % len(color_options)
                        # Cambiamos el color de la nave al seleccionado
                        nave_color = color_options[current_color_index]["color"]
                    elif selected_option == 1:  # Si estamos en Velocidad de Enemigos
                        # Movemos a la siguiente opción (o a la primera si estamos en la última)
                        current_speed_index = (current_speed_index + 1) % len(speed_options)
                        # Cambiamos la velocidad de los enemigos a la seleccionada
                        enemy_speed_multiplier = speed_options[current_speed_index]["value"]
                
                if event.key == pygame.K_RETURN:  # Si presiona Enter (para seleccionar)
                    if selected_option == 2:  # Si estamos en Guardar y Volver
                        return  # Volvemos al menú principal guardando los cambios
                
                if event.key == pygame.K_ESCAPE:  # Si presiona Escape
                    return  # Volvemos al menú principal
        
        # Pintamos el fondo del menú de opciones
        screen.fill(MENU_BG)
        
        # Si tenemos imagen de fondo, la usamos con un efecto semitransparente
        if background_img:
            # Hacemos una copia de la imagen y la oscurecemos para el menú
            menu_bg = background_img.copy()
            dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            dark_surface.fill((0, 0, 0, 180))  # Negro más oscuro que en el menú principal
            menu_bg.blit(dark_surface, (0, 0))
            screen.blit(menu_bg, (0, 0))
        
        # Dibujamos el título de opciones
        title_text = title_font.render("OPCIONES", True, WHITE)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 100))
        
        # Lista de opciones que podemos cambiar
        options = ["Color de la Nave", "Velocidad de Enemigos", "Guardar y Volver"]
        
        # Dibujamos cada opción del menú
        for i, option in enumerate(options):
            # Si esta opción está seleccionada, la pintamos amarilla, si no, blanca
            text_color = YELLOW if i == selected_option else WHITE
            
            # Mostramos el texto de la opción
            option_text = option_font.render(option, True, text_color)
            
            # La opción "Guardar y Volver" va más abajo que las otras
            y_pos = 220 + i * 100 if i < 2 else 450
            
            screen.blit(option_text, (WIDTH//2 - option_text.get_width()//2, y_pos))
            
            # Si es una opción que tiene un valor, mostramos el valor actual
            if i == 0:  # Color de Nave
                # Mostramos el nombre del color actual
                value_text = option_font.render(color_options[current_color_index]["name"], True, color_options[current_color_index]["color"])
                screen.blit(value_text, (WIDTH//2 - value_text.get_width()//2, y_pos + 40))
                
                # Dibujamos una muestra del color actual
                pygame.draw.rect(screen, color_options[current_color_index]["color"], (WIDTH//2 - 25, y_pos + 80, 50, 20))
                
                # Si esta opción está seleccionada, dibujamos flechas para indicar que podemos cambiarla
                if selected_option == 0:
                    left_arrow = pygame.font.SysFont(None, 50).render("◀", True, WHITE)
                    right_arrow = pygame.font.SysFont(None, 50).render("▶", True, WHITE)
                    screen.blit(left_arrow, (WIDTH//2 - 100, y_pos + 40))
                    screen.blit(right_arrow, (WIDTH//2 + 100, y_pos + 40))
            
            elif i == 1:  # Velocidad de Enemigos
                # Mostramos el nombre de la velocidad actual
                value_text = option_font.render(speed_options[current_speed_index]["name"], True, WHITE)
                screen.blit(value_text, (WIDTH//2 - value_text.get_width()//2, y_pos + 40))
                
                # Dibujamos una barra que representa la velocidad
                bar_width = 200  # Ancho total de la barra
                bar_x = WIDTH//2 - bar_width//2  # Posición X de la barra (centrada)
                # Dibujamos el borde de la barra
                pygame.draw.rect(screen, WHITE, (bar_x, y_pos + 80, bar_width, 10), 1)
                
                # Calculamos cuánto de la barra debe estar lleno según la velocidad
                fill_width = int(bar_width * (speed_options[current_speed_index]["value"] / speed_options[-1]["value"]))
                # Rellenamos la barra con color según la velocidad
                # Verde para velocidades lentas, naranja para rápido, rojo para muy rápido
                fill_color = GREEN if current_speed_index < 2 else ORANGE if current_speed_index == 2 else RED
                pygame.draw.rect(screen, fill_color, (bar_x, y_pos + 80, fill_width, 10))
                
                # Si esta opción está seleccionada, dibujamos flechas para indicar que podemos cambiarla
                if selected_option == 1:
                    left_arrow = pygame.font.SysFont(None, 50).render("◀", True, WHITE)
                    right_arrow = pygame.font.SysFont(None, 50).render("▶", True, WHITE)
                    screen.blit(left_arrow, (WIDTH//2 - 120, y_pos + 40))
                    screen.blit(right_arrow, (WIDTH//2 + 120, y_pos + 40))
        
        # Añadimos instrucciones en la parte inferior
        instructions = pygame.font.SysFont(None, 24).render(
            "Usa ↑↓ para moverte, ←→ para cambiar valores y ENTER para guardar", True, WHITE)
        screen.blit(instructions, (WIDTH//2 - instructions.get_width()//2, HEIGHT - 50))
        
        # Actualizamos la pantalla para que se vean los cambios
        pygame.display.update()
        
        # Controlamos la velocidad de actualización del menú
        pygame.time.Clock().tick(30)  # 30 imágenes por segundo

# ======== 8. FUNCIÓN PRINCIPAL ========
# Función principal del juego (¡aquí ocurre toda la acción!)
def main(mode="normal"):
    player = Player(color=nave_color)  # Creamos al jugador con el color seleccionado
    enemies = []  # Lista para guardar a los enemigos
    fast_enemies = []  # Lista para los enemigos rápidos (solo en modo desafío)
    boss = None  # Variable para el jefe (solo en modo desafío)
    clock = pygame.time.Clock()  # Reloj para controlar la velocidad del juego
    score = 0  # Puntuación inicial
    game_over = False  # El juego no ha terminado
    level = 1  # Empezamos en el nivel 1
    
    # Configuramos la letra para mostrar texto
    font = pygame.font.SysFont(None, 36)  # Tipo y tamaño de letra
    
    # Creamos los enemigos iniciales (formando filas y columnas)
    for i in range(6):  # 6 columnas
        for j in range(3):  # 3 filas
            enemy = Enemy(100 + i * 100, 50 + j * 70, speed_multiplier=enemy_speed_multiplier)  # Posición de cada enemigo con la velocidad seleccionada
            enemies.append(enemy)  # Añadimos el enemigo a la lista
    
    # En modo desafío, añadimos algunos enemigos rápidos
    if mode == "desafio":
        for i in range(3):  # 3 enemigos rápidos
            fast_enemy = FastEnemy(200 + i * 150, 30, speed_multiplier=enemy_speed_multiplier)
            fast_enemies.append(fast_enemy)
    
    # Bucle principal del juego (se repite constantemente mientras jugamos)
    while True:
        # Comprobamos si el jugador quiere hacer algo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si el jugador cierra la ventana
                pygame.quit()  # Cerramos pygame
                sys.exit()  # Salimos del programa
            
            if event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_SPACE and not game_over:  # Si es la barra espaciadora y el juego no ha terminado
                    player.shoot()  # Disparamos un láser
                if event.key == pygame.K_RETURN and game_over:  # Si es Enter y el juego ha terminado
                    # Volvemos al menú principal
                    return
                if event.key == pygame.K_ESCAPE:  # Si es Escape
                    return  # Volvemos al menú principal
        
        if game_over:
            # Si el juego ha terminado, mostramos la pantalla de "Game Over"
            screen.fill(BLACK)  # Fondo negro
            
            # Preparamos los textos que queremos mostrar
            game_over_text = font.render("¡Juego Terminado!", True, WHITE)  # Mensaje de fin
            score_text = font.render(f"Puntuación: {score}", True, WHITE)  # Puntuación final
            level_text = font.render(f"Nivel alcanzado: {level}", True, LIGHT_BLUE)  # Nivel final
            
            if mode == "desafio":
                mode_text = font.render("Modo: DESAFÍO", True, ORANGE)  # Indicamos que era modo desafío
            else:
                mode_text = font.render("Modo: Normal", True, WHITE)  # Indicamos que era modo normal
                
            restart_text = font.render("Presiona ENTER para volver al menú", True, WHITE)  # Instrucción para reiniciar
            
            # Mostramos los textos en la pantalla, centrados
            screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 100))
            screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 50))
            screen.blit(level_text, (WIDTH//2 - level_text.get_width()//2, HEIGHT//2))
            screen.blit(mode_text, (WIDTH//2 - mode_text.get_width()//2, HEIGHT//2 + 50))
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 100))
            
            pygame.display.update()  # Actualizamos la pantalla
            continue  # Volvemos al inicio del bucle (no procesamos el resto)
        
        # Controlamos el movimiento del jugador con las flechas del teclado
        keys = pygame.key.get_pressed()  # Obtenemos qué teclas están presionadas
        if keys[pygame.K_LEFT]:  # Si presionamos la flecha izquierda
            player.move("left")  # Movemos la nave a la izquierda
        if keys[pygame.K_RIGHT]:  # Si presionamos la flecha derecha
            player.move("right")  # Movemos la nave a la derecha
        
        # Actualizamos la posición de todos los láseres
        player.update_lasers()
        
        # Controlamos el movimiento de los enemigos
        # Ya no necesitamos verificar límites aquí, cada enemigo lo hace por sí mismo
        for enemy in enemies:
            enemy.move()  # Movemos al enemigo
            
            # Si un enemigo llega a la altura de nuestra nave
            if enemy.y + enemy.height >= player.y:
                game_over = True  # El juego termina
        
        # En modo desafío, movemos también los enemigos rápidos
        if mode == "desafio":
            # Mover enemigos rápidos
            for enemy in fast_enemies:
                enemy.move()
                
                # Si un enemigo rápido llega a la altura de nuestra nave
                if enemy.y + enemy.height >= player.y:
                    game_over = True  # El juego termina
            
            # Si hay un jefe, lo movemos
            if boss:
                boss.move()
                
                # Si el jefe llega a la altura de nuestra nave
                if boss.y + boss.height >= player.y:
                    game_over = True  # El juego termina
        
        # Comprobamos si algún láser golpea a algún enemigo
        for laser in player.lasers[:]:
            hit = False  # Por defecto, no hay impacto
            
            # Verificar colisión con enemigos normales
            for enemy in enemies[:]:
                if check_collision(laser, enemy):  # Si el láser golpea al enemigo
                    player.lasers.remove(laser)  # Quitamos el láser
                    enemies.remove(enemy)  # Quitamos al enemigo
                    score += 10  # Aumentamos la puntuación
                    hit = True  # Hubo un impacto
                    break
            
            # Si ya hubo un impacto, pasamos al siguiente láser
            if hit:
                continue
            
            # En modo desafío, verificar colisión con enemigos rápidos
            if mode == "desafio":
                for enemy in fast_enemies[:]:
                    if check_collision(laser, enemy):
                        player.lasers.remove(laser)
                        fast_enemies.remove(enemy)
                        score += 20  # Los enemigos rápidos dan más puntos
                        hit = True
                        break
                
                # Si ya hubo un impacto, pasamos al siguiente láser
                if hit:
                    continue
                
                # Verificar colisión con el jefe
                if boss and check_collision(laser, boss):
                    player.lasers.remove(laser)
                    boss.health -= 1  # El jefe pierde una vida
                    
                    # Si el jefe se queda sin vida
                    if boss.health <= 0:
                        boss = None  # Eliminamos al jefe
                        score += 100  # El jefe da muchos puntos
        
        # Si no quedan enemigos, pasamos al siguiente nivel
        if len(enemies) == 0 and len(fast_enemies) == 0 and boss is None:
            level += 1  # Aumentamos el nivel
            
            # Creamos nuevos enemigos (más rápidos que en el nivel anterior)
            for i in range(6):
                for j in range(3):
                    enemy = Enemy(100 + i * 100, 50 + j * 70, speed_multiplier=enemy_speed_multiplier)
                    # La velocidad aumenta un 5% con cada nivel pero también respeta el multiplicador del usuario
                    enemy.base_speed = 1 + level * 0.05  # Aumentamos la velocidad base un 5% por nivel
                    enemy.speed = enemy.base_speed * enemy_speed_multiplier  # Aplicamos el multiplicador
                    enemies.append(enemy)
            
            # En modo desafío, añadimos enemigos rápidos en niveles pares
            if mode == "desafio":
                # En niveles pares añadimos enemigos rápidos
                if level % 2 == 0:
                    for i in range(level // 2):  # Más enemigos rápidos en niveles superiores
                        fast_enemy = FastEnemy(100 + i * 150, 30, speed_multiplier=enemy_speed_multiplier)
                        # Los enemigos rápidos también aumentan su velocidad un 5% por nivel
                        fast_enemy.base_speed = 2 + level * 0.05  # Aumentamos la velocidad base un 5% por nivel
                        fast_enemy.speed = fast_enemy.base_speed * enemy_speed_multiplier  # Aplicamos el multiplicador
                        fast_enemies.append(fast_enemy)
                
                # En niveles divisibles por 3, añadimos un jefe
                if level % 3 == 0:
                    boss = Boss(WIDTH // 2 - 40, 50, speed_multiplier=enemy_speed_multiplier)
                    boss.health = 5 + level // 3  # El jefe tiene más vida en niveles superiores
                    # El jefe también aumenta su velocidad un 5% por nivel
                    boss.base_speed = 1.5 + level * 0.05  # Aumentamos la velocidad base un 5% por nivel
                    boss.speed = boss.base_speed * enemy_speed_multiplier  # Aplicamos el multiplicador
        
        # Dibujamos todo en la pantalla
        if background_img:  # Si tenemos imagen de fondo
            screen.blit(background_img, (0, 0))  # La mostramos
        else:  # Si no tenemos imagen
            screen.fill(BLACK)  # Pintamos la pantalla de negro
        
        # Dibujamos la nave del jugador
        player.draw()
        
        # Dibujamos todos los láseres
        for laser in player.lasers:
            laser.draw()
        
        # Dibujamos todos los enemigos
        for enemy in enemies:
            enemy.draw()
        
        # En modo desafío, dibujamos los enemigos rápidos y el jefe
        if mode == "desafio":
            for enemy in fast_enemies:
                enemy.draw()
            
            if boss:
                boss.draw()
        
        # Mostramos la puntuación y el nivel actual
        score_text = font.render(f"Puntuación: {score}", True, WHITE)
        level_text = font.render(f"Nivel: {level}", True, WHITE)
        
        # En modo desafío, mostramos el modo de juego
        if mode == "desafio":
            mode_text = font.render("¡MODO DESAFÍO!", True, ORANGE)
            screen.blit(mode_text, (WIDTH // 2 - mode_text.get_width() // 2, 10))
        
        screen.blit(score_text, (10, 10))  # Puntuación en la esquina superior izquierda
        screen.blit(level_text, (WIDTH - 120, 10))  # Nivel en la esquina superior derecha
        
        # Mostramos instrucción para volver al menú
        esc_text = pygame.font.SysFont(None, 20).render("Presiona ESC para volver al menú", True, WHITE)
        screen.blit(esc_text, (10, HEIGHT - 30))
        
        # Actualizamos la pantalla para mostrar todo lo que hemos dibujado
        pygame.display.update()
        
        # Controlamos la velocidad del juego (60 fotogramas por segundo)
        clock.tick(60)  # Como si fueran 60 páginas de un libro animado por segundo

# ======== 9. FUNCIÓN MODO DESAFÍO ========
# Función para el modo especial con jefes y enemigos rápidos
def challenge_mode():
    # Implementa la lógica para el modo desafío
    pass

# ======== 10. INICIO DEL JUEGO ========
# Iniciamos el juego cuando ejecutamos este archivo
if __name__ == "__main__":  # Esto significa "si estamos ejecutando este archivo directamente"
    while True:
        # Mostramos el menú principal
        game_mode = show_menu()
        
        # Iniciamos el juego en el modo seleccionado
        main(game_mode) 