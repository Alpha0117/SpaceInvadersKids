@echo off
color 0A
echo =====================================
echo =   SPACE INVADERS PARA NINOS      =
echo =       ¡AVENTURA ESPACIAL!        =
echo =====================================
echo.
echo Preparando tu nave espacial...
timeout /t 1 >nul
echo Cargando armas laser...
timeout /t 1 >nul
echo Detectando alienígenas...
timeout /t 1 >nul
echo.
echo ¡Preparando todo para tu misión espacial!
py create_images.py
echo.
echo ¡Todo listo, piloto! Iniciando el juego...
echo.
echo Controles: Flechas para mover, ESPACIO para disparar
echo.
echo Cargando juego en 3...
timeout /t 1 >nul
echo Cargando juego en 2...
timeout /t 1 >nul
echo Cargando juego en 1...
timeout /t 1 >nul
echo ¡DESPEGUE!
py main.py
echo.
echo ¡Gracias por jugar! Presiona cualquier tecla para salir.
pause 