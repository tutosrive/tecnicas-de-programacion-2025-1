"""
- write(): Escribe una cadena en el archivo.
- writelines(): Escribe una lista de cadenas en el archivo.

Modos:
    - 'w': Sobrescribe el archivo existente.
    - 'a': Agrega contenido al final del archivo
"""
file_path = './manipulacion_archivos/explicacion/data/new_my_file.txt'

# Escribir en un archivo (sobrescribe)
with open(file_path, 'w') as file:
    file.write('Overwritten content.\n')
# Agregar al final del archivo
with open(file_path, 'a') as file:
    file.write('This is an appended line.\n')