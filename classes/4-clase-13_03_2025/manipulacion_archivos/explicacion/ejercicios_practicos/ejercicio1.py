"""
Crear, Escribir y Leer un Archivo en Python

Objetivo:
    1. Crear un archivo de texto llamado mi_archivo.txt.
    2. Escribir varias líneas de texto en el archivo.
    3. Leer el contenido del archivo línea por línea y mostrarlo en la consola
"""
data_exercise_path = './explicacion/ejercicios_practicos/data'

# Abrir el archivo 'mi_archivo.txt' en modo de escritura (Con acentos)
with open(f'{data_exercise_path}/mi_archivo.txt', 'w', encoding="utf-8") as archivo:
    # Lista de líneas a escribir
    lineas = [
        "Esta es la primera línea.\n",
        "Aquí va la segunda línea.\n",
        "Y finalmente, la tercera línea.\n",
        "Esta vez si la línea final.\n"
    ]
    # Escribir las líneas en el archivo
    archivo.writelines(lineas)

# Lectura del archivo
# Abrir el archivo 'mi_archivo.txt' en modo de lectura
with open(f'{data_exercise_path}/mi_archivo.txt', 'r', encoding="utf-8") as archivo:
    # Leer el archivo línea por línea
    for linea in archivo:
        # Mostrar cada línea en la consola
        print(linea.strip())  # strip() elimina el salto de línea al final