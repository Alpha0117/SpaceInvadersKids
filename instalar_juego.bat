@echo off
color 0A
echo =====================================
echo =   INSTALACION SPACE INVADERS     =
echo =       PARA NINOS                 =
echo =====================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python no esta instalado en tu sistema.
    echo Por favor, instala Python desde https://www.python.org/downloads/
    echo Asegurate de marcar la opcion "Add Python to PATH" durante la instalacion.
    echo.
    echo Presiona cualquier tecla para salir...
    pause >nul
    exit /b 1
)

echo Python encontrado! Comenzando instalacion...
echo.

REM Crear un entorno virtual
echo Creando entorno virtual...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error al crear el entorno virtual.
    echo Comprueba que tienes instalado el modulo venv.
    echo Puedes instalarlo ejecutando: python -m pip install virtualenv
    echo.
    echo Presiona cualquier tecla para salir...
    pause >nul
    exit /b 1
)

REM Activar el entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo Instalando pygame...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error al instalar las dependencias.
    echo.
    echo Presiona cualquier tecla para salir...
    pause >nul
    exit /b 1
)

echo.
echo =====================================
echo =  INSTALACION COMPLETADA CON      =
echo =          EXITO!                  =
echo =====================================
echo.
echo Para jugar, ejecuta el archivo 'jugar.bat'
echo.

REM Crear el archivo jugar.bat para ejecutar el juego
echo @echo off > jugar.bat
echo color 0A >> jugar.bat
echo echo Activando entorno virtual... >> jugar.bat
echo call venv\Scripts\activate.bat >> jugar.bat
echo. >> jugar.bat
echo echo Iniciando Space Invaders para Ninos... >> jugar.bat
echo echo. >> jugar.bat
echo echo Controles: >> jugar.bat
echo echo - Flechas IZQUIERDA y DERECHA para mover la nave >> jugar.bat
echo echo - ESPACIO para disparar >> jugar.bat
echo echo - ESC para volver al menu >> jugar.bat
echo echo. >> jugar.bat
echo echo Preparando lanzamiento en 3... >> jugar.bat
echo timeout /t 1 ^>nul >> jugar.bat
echo echo Preparando lanzamiento en 2... >> jugar.bat
echo timeout /t 1 ^>nul >> jugar.bat
echo echo Preparando lanzamiento en 1... >> jugar.bat
echo timeout /t 1 ^>nul >> jugar.bat
echo echo DESPEGUE! >> jugar.bat
echo. >> jugar.bat
echo python main.py >> jugar.bat
echo. >> jugar.bat
echo echo Gracias por jugar! Presiona cualquier tecla para salir... >> jugar.bat
echo pause ^>nul >> jugar.bat
echo exit >> jugar.bat

echo Presiona cualquier tecla para salir...
pause >nul 