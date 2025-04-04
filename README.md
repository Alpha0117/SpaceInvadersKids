# 🚀 Space Invaders para Niños 👾

Un juego educativo de naves espaciales diseñado para enseñar programación a niños de 7 a 16 años.

![Space Invaders para Niños](https://raw.githubusercontent.com/usuario/SpaceInvadersKids/main/imagenes/screenshot.png)

## 📋 Descripción

Este juego es una versión simplificada de Space Invaders, con código bien documentado y diseñado específicamente para que los niños puedan entender cómo funciona un videojuego. Es divertido jugar y también sirve como herramienta educativa para aprender conceptos básicos de programación.

## 🎮 Características

- Controles sencillos: flechas izquierda/derecha para mover, espacio para disparar
- Modos de juego: normal y desafío
- Personalización de la nave y velocidad de los enemigos
- Niveles progresivos con dificultad creciente
- Código altamente comentado para fines educativos

## 💻 Requisitos del sistema

- Python 3.6 o superior
- Pygame 2.0.0 o superior

## 🔧 Instalación

### En Windows

#### Método 1: Instalación con entorno virtual (recomendado)

1. **Descarga el juego**
   - Descarga o clona este repositorio a tu computadora

2. **Instala Python**
   - Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/)
   - Asegúrate de marcar la opción "Add Python to PATH" durante la instalación

3. **Ejecuta el script de instalación**
   - Navega a la carpeta del juego
   - Haz doble clic en el archivo `instalar_juego.bat`
   - Este script creará un entorno virtual e instalará todas las dependencias necesarias

4. **Juega**
   - Una vez finalizada la instalación, se creará automáticamente un archivo `jugar.bat`
   - Haz doble clic en `jugar.bat` cada vez que quieras jugar

#### Método 2: Inicio rápido (sin entorno virtual)

1. **Instala Python y Pygame**
   - Asegúrate de tener Python instalado
   - Instala Pygame usando el comando: `pip install pygame`

2. **Ejecuta el juego directamente**
   - Haz doble clic en `iniciar_juego.bat` para empezar a jugar

### En Linux

#### Método 1: Instalación con entorno virtual (recomendado)

1. **Descarga el juego**
   ```bash
   git clone https://github.com/usuario/SpaceInvadersKids.git
   cd SpaceInvadersKids
   ```

2. **Da permisos de ejecución a los scripts**
   ```bash
   chmod +x install_game.sh iniciar_juego.sh
   ```

3. **Ejecuta el script de instalación**
   ```bash
   ./install_game.sh
   ```
   Este script verificará si Python está instalado, creará un entorno virtual e instalará todas las dependencias.

4. **Juega**
   ```bash
   ./play.sh
   ```
   Usa este comando cada vez que quieras jugar.

#### Método 2: Inicio rápido (sin entorno virtual)

1. **Instala Python y Pygame**
   - En Ubuntu/Debian:
     ```bash
     sudo apt install python3 python3-pip
     pip3 install pygame
     ```
   - En Fedora:
     ```bash
     sudo dnf install python3 python3-pip
     pip3 install pygame
     ```
   - En Arch:
     ```bash
     sudo pacman -S python python-pip
     pip install pygame
     ```

2. **Ejecuta el juego directamente**
   ```bash
   ./iniciar_juego.sh
   ```

## 🎯 Cómo jugar

1. **Menú principal**
   - Usa las flechas ↑/↓ para navegar por las opciones
   - Presiona ENTER para seleccionar una opción

2. **Controles en el juego**
   - Flecha IZQUIERDA: Mover la nave a la izquierda
   - Flecha DERECHA: Mover la nave a la derecha
   - ESPACIO: Disparar rayos láser
   - ESC: Volver al menú principal

3. **Objetivos**
   - Destruye a todos los alienígenas para avanzar al siguiente nivel
   - Evita que los alienígenas lleguen a la parte inferior de la pantalla
   - ¡Consigue la mayor puntuación posible!

## 🔄 Personalización

El juego ofrece opciones de personalización accesibles desde el menú:

1. **Color de la nave**: Elige entre varios colores para tu nave espacial
2. **Velocidad de los enemigos**: Ajusta la dificultad del juego cambiando la velocidad de los alienígenas

## 👨‍👩‍👧‍👦 Para padres y educadores

Este juego ha sido diseñado como una herramienta educativa. Recomendamos:

1. Jugar primero con los niños para familiarizarlos con el juego
2. Explorar el código juntos, aprovechando los detallados comentarios
3. Proponer pequeños cambios (como colores o velocidades) para entender cómo funciona

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el juego o añadir nuevas características educativas, por favor:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## 🙏 Agradecimientos

- [Pygame](https://www.pygame.org/) por proporcionar una biblioteca fantástica para crear juegos en Python
- A todos los educadores que utilizan la programación de juegos como herramienta de enseñanza 