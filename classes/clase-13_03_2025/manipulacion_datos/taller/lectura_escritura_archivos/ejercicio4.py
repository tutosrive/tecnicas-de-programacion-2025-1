"""
Enunciado:
    Modifique un archivo notas.txt agregando nuevas calificaciones al final.
"""
from paths import data_path
with open(f'{data_path}/notas.txt', 'a') as file:
    notes: list[str] = ["4.2", "1.8", "4.1", "3.3", "\n"]
    file.writelines(notes)