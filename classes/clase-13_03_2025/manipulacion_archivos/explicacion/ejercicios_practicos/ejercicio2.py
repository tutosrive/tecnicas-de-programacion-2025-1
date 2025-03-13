"""
Leer un Archivo CSV y Calcular el Promedio de una Columna

Objetivo:
    1. Crear un archivo CSV llamado datos.csv con información ficticia.
    2. Leer los datos de este archivo.
    3. Calcular el promedio de una columna numérica específica (por ejemplo, "Edad").
"""
data_path = './manipulacion_archivos/explicacion/ejercicios_practicos/data'

import csv  # Importar el módulo CSV para manipular archivos CSV

# Paso 1: Crear y escribir en el archivo CSV
with open(f'{data_path}/datos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    # Escribir la fila de encabezado
    escritor_csv.writerow(['Nombre', 'Edad', 'Ciudad'])
    # Escribir las filas de datos
    escritor_csv.writerows([
        ['Ana', 23, 'Madrid'],
        ['Luis', 29, 'Barcelona'],
        ['Clara', 32, 'Valencia'],
        ['Juan', 26, 'Sevilla'],
        ['Eva', 24, 'Bilbao'],
        ['Santiago', 19, "Fresno"]
    ])

# Paso 2: Leer el archivo CSV y calcular el promedio de la columna "Edad"
with open(f'{data_path}/datos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Saltar la fila de encabezado
    edades = []  # Lista para almacenar las edades
    for fila in lector_csv:
        edad = int(fila[1])  # Convertir la edad a entero
        edades.append(edad)

    # Calcular el promedio de edades
    if edades:
        promedio = sum(edades) / len(edades)
        print(f"El promedio de edad es: {promedio:.2f}") # Formatear a máximo 2 decimales
    else:
        print("No hay edades disponibles para calcular el promedio.")
