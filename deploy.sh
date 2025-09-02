#!/bin/bash
set -e

APP_NAME="pdf-reader"

echo "🚀 Desplegando $APP_NAME ..."

# Detener contenedor si ya está corriendo
if [ "$(docker ps -q -f name=$APP_NAME)" ]; then
  echo "🛑 Deteniendo contenedor existente..."
  docker stop $APP_NAME || true
  docker rm $APP_NAME || true
fi

# Reconstruir y levantar con docker-compose
echo "📦 Construyendo imagen y levantando servicio..."
docker-compose up -d --build

# Mostrar estado
echo "✅ Contenedores en ejecución:"
docker ps | grep $APP_NAME

echo "🌐 API disponible en: http://$(curl -s ifconfig.me -4):5000/read_pdf"
