@echo off

echo Validando la instalación de Go...

REM Verificar si Go está instalado
where go > nul 2>&1
if %errorlevel% neq 0 (
    echo Go no está instalado en el sistema. Se procederá a la instalación de Go.

    REM Descargar el instalador de Go
    echo Descargando el instalador de Go...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://golang.org/dl/go{{GO_VERSION}}.{{OS}}-{{ARCH}}.msi' -OutFile 'go-installer.msi'}"

    REM Instalar Go
    echo Instalando Go...
    start /wait msiexec /i go-installer.msi

    REM Verificar nuevamente si Go está instalado
    where go > nul 2>&1
    if %errorlevel% neq 0 (
        echo No se pudo instalar Go. Asegúrate de instalarlo manualmente desde https://golang.org/dl/
        pause
        exit /b 1
    )

    echo Go se ha instalado correctamente.
    echo.
)

echo Validando la instalación de Python...

REM Verificar si Python está instalado
where python3 > nul 2>&1
if %errorlevel% neq 0 (
    echo Python no está instalado en el sistema. Se procederá a la instalación de Python.

    REM Descargar el instalador de Python
    echo Descargando el instalador de Python...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/{{PYTHON_VERSION}}/python-{{PYTHON_VERSION}}.{{OS}}-{{ARCH}}.msi' -OutFile 'python-installer.msi'}"

    REM Instalar Python
    echo Instalando Python...
    start /wait msiexec /i python-installer.msi

    REM Verificar nuevamente si Python está instalado
    where python3 > nul 2>&1
    if %errorlevel% neq 0 (
        echo No se pudo instalar Python. Asegúrate de instalarlo manualmente desde https://www.python.org/
        pause
        exit /b 1
    )

    echo Python se ha instalado correctamente.
    echo.
)

REM Verificar si se encuentra en el directorio correcto del proyecto de Python
if not exist interfaz.py (
    echo No se encuentra en el directorio correcto del proyecto de Python. Asegúrate de ejecutar el script en el directorio correcto.
    pause
    exit /b 1
)

REM Ejecutar el proyecto de Python
start cmd.exe /K "python3 .\interfaz.py"
