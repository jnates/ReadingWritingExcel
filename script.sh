#!/bin/bash

echo "Instalando paquetes..."

# Instalar Go si no está instalado
if ! command -v go &> /dev/null; then
    echo "Go no está instalado en el sistema. Por favor, instala Go antes de continuar."
    exit 1
fi

# Verificar si se encuentra en un directorio de proyecto de Go
if [ ! -f go.mod ]; then
    echo "No se encuentra en un directorio de proyecto de Go. Asegúrate de ejecutar el script en el directorio correcto."
    exit 1
fi

# Actualizar y descargar las dependencias del proyecto
go mod tidy
go mod download

if [[ $? -ne 0 ]]; then
    echo "Error al actualizar o descargar las dependencias del proyecto."
    exit 1
fi

echo "Las dependencias se han instalado correctamente."
