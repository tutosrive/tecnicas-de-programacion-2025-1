"""
Enunciado:
    Cree un programa que escriba en un archivo datos.txt la frase "Python es divertido".

Pseudocódigo:
    ABRIR ARCHIVO 'datos.txt' EN MODO ESCRITURA
    ESCRIBIR EN ARCHIVO "Python es divertido"
    CERRAR ARCHIVO
"""
from paths import datos_file

with open(datos_file, 'w') as file:
    file.write('Python es divertido')