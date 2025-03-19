"""
Enunciado:
    Lea un archivo con datos de estudiantes y almacénelos en una lista de listas.
"""
import csv

data: list[list[str]] = []
with open('./listas/data/estudiantes.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    # Omitir encabezado
    next(csv_reader)
    # csv, por defecto trae una lista de listas
    data = list(csv.reader(file))

print(data)