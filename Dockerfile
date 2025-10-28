# Usa una imagen liviana de Python
FROM python:3.13-alpine

# Instala dependencias básicas
RUN apk add --no-cache gcc musl-dev libffi-dev

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto donde correrá Django
EXPOSE 8000

# Comando por defecto para correr la app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
