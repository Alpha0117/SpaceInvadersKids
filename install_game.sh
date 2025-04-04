#!/bin/bash

# Colores para el terminal
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}=====================================${NC}"
echo -e "${GREEN}=   INSTALACION SPACE INVADERS     =${NC}"
echo -e "${GREEN}=       PARA NIÑOS                 =${NC}"
echo -e "${GREEN}=====================================${NC}"
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python no está instalado en tu sistema."
    echo "Por favor, instala Python con tu gestor de paquetes:"
    echo "  Para Ubuntu/Debian: sudo apt install python3 python3-pip python3-venv"
    echo "  Para Fedora: sudo dnf install python3 python3-pip"
    echo "  Para Arch: sudo pacman -S python python-pip"
    echo ""
    echo "Presiona ENTER para salir..."
    read
    exit 1
fi

echo "Python encontrado! Comenzando instalación..."
echo ""

# Crear un entorno virtual
echo "Creando entorno virtual..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error al crear el entorno virtual."
    echo "Comprueba que tienes instalado el módulo venv:"
    echo "  Para Ubuntu/Debian: sudo apt install python3-venv"
    echo "  Para Fedora: sudo dnf install python3-venv"
    echo "  Para Arch: ya viene incluido con python"
    echo ""
    echo "Presiona ENTER para salir..."
    read
    exit 1
fi

# Activar el entorno virtual
echo "Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "Instalando pygame..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error al instalar las dependencias."
    echo ""
    echo "Presiona ENTER para salir..."
    read
    exit 1
fi

echo ""
echo -e "${GREEN}=====================================${NC}"
echo -e "${GREEN}=  INSTALACION COMPLETADA CON      =${NC}"
echo -e "${GREEN}=          EXITO!                  =${NC}"
echo -e "${GREEN}=====================================${NC}"
echo ""
echo "Para jugar, ejecuta el archivo 'play.sh'"
echo ""

# Crear el archivo play.sh para ejecutar el juego
cat > play.sh << 'EOL'
#!/bin/bash

# Colores para el terminal
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo "Activando entorno virtual..."
source venv/bin/activate

echo -e "${GREEN}Iniciando Space Invaders para Niños...${NC}"
echo ""
echo "Controles:"
echo "- Flechas IZQUIERDA y DERECHA para mover la nave"
echo "- ESPACIO para disparar"
echo "- ESC para volver al menú"
echo ""
echo "Preparando lanzamiento en 3..."
sleep 1
echo "Preparando lanzamiento en 2..."
sleep 1
echo "Preparando lanzamiento en 1..."
sleep 1
echo -e "${GREEN}¡DESPEGUE!${NC}"
echo ""

python3 main.py

echo ""
echo "Gracias por jugar! Presiona ENTER para salir..."
read
EOL

# Dar permisos de ejecución a play.sh
chmod +x play.sh

echo "Presiona ENTER para salir..."
read 