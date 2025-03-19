"""
Enunciado:
    Lea un archivo de texto línea por línea e imprima el número total de líneas.
"""

from paths import data_path

with open(f'{data_path}/notas.txt', 'r') as file:
    lines: list[str] = file.readlines()
    print(f'El archivo "notas.txt" tiene {len(lines)} líneas.')