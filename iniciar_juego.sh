#!/bin/bash

# Colores para el terminal
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}=====================================${NC}"
echo -e "${GREEN}=   SPACE INVADERS PARA NIÑOS      =${NC}"
echo -e "${GREEN}=       ¡AVENTURA ESPACIAL!        =${NC}"
echo -e "${GREEN}=====================================${NC}"
echo ""

echo "Preparando tu nave espacial..."
sleep 1
echo "Cargando armas láser..."
sleep 1
echo "Detectando alienígenas..."
sleep 1
echo ""

echo "¡Preparando todo para tu misión espacial!"
python3 create_images.py
echo ""

echo -e "${GREEN}¡Todo listo, piloto! Iniciando el juego...${NC}"
echo ""
echo "Controles: Flechas para mover, ESPACIO para disparar"
echo ""
echo "Cargando juego en 3..."
sleep 1
echo "Cargando juego en 2..."
sleep 1
echo "Cargando juego en 1..."
sleep 1
echo -e "${GREEN}¡DESPEGUE!${NC}"

python3 main.py

echo ""
echo "¡Gracias por jugar! Presiona ENTER para salir."
read 