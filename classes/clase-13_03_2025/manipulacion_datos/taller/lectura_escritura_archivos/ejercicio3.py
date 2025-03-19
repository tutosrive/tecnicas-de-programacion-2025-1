"""
Enunciado:
    Escriba un programa que lea un archivo con nombres y los almacene en una lista.
"""

from paths import data_path

with open(f'{data_path}/names.txt', 'r', encoding='utf-8') as file:
    names: list[str] = file.readlines()
    print(names)