"""
Enunciado:
    Lea el contenido del archivo datos.txt e imprímalo en pantalla.

Pseudocódigo:
    ABRIR ARCHIVO 'datos.txt' EN MODO LECTURA
    LEER DATOS ED ARCHIVO
    ESCRIBIR DATOS OBTENIDOS DEL ARCHIVO
    CERRAR ARCHIVO
"""
from paths import datos_file

with open(datos_file, 'r') as file:
    data: str = file.read()
    print(data)