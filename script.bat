@echo off

echo Instalando paquetes...

REM Verificar si Go está instalado
where go > nul 2>&1
if %errorlevel% neq 0 (
    echo Go no está instalado en el sistema. Se procederá a la instalación de Go.

    REM Descargar el instalador de Go
    echo Descargando el instalador de Go...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://golang.org/dl/go{{VERSION}}.{{OS}}-{{ARCH}}.msi' -OutFile 'go-installer.msi'}"

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
    echo Por favor, vuelve a ejecutar este script para continuar.
    pause
    exit /b
)

REM Verificar si se encuentra en un directorio de proyecto de Go
if not exist go.mod (
    echo No se encuentra en un directorio de proyecto de Go. Asegúrate de ejecutar el script en el directorio correcto.
    pause
    exit /b 1
)

REM Ejecutar el comando para instalar las dependencias y ejecutar el archivo main.go
start cmd.exe /K "go mod tidy && go mod download && go run main.go"
