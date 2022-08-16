# Descarga la imagen de Python 3.9
FROM python:3.9

# Ubicación del proyecto en el SO de la imagen de Python
WORKDIR /app

# Copia el contenido del directorio actual en /app - Se copia el código fuente actual
COPY . /app 

#  Descargar e instala los paquetes necesarios para el proyecto
RUN pip3 --no-cache-dir install -r requirements.txt

# Ejecuta app.py cuando el contenedor se inicia
CMD [ "python3", "src/app.py" ]


 