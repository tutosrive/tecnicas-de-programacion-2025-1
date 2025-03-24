"""
Enunciado:
    Divida una cadena en palabras y cuente cuántas tiene.

Pseudocódigo:
    ESCIRBIR "Ingrese una frase: "
    LEER phrase

    words_list <- phrase.split(' ')
    words_count <- words_list.length()

    ESCRIBIR "La frase tiene ", words_count, " palabras."

Estrategia:
    Se plantea dividir el String por medio de los espacios ingresados, y la longitud de la lista resultante, será
    el conteo de palabras en la frase (nuevamente se reutiliza la función splitter)
"""

from ejercicio2 import splitter

# Ingreso de información
phrase: str = input("Ingrese una frase: ")

# Dividir la frase/string por medio de los "espacios"
words_list: list = splitter(phrase, " ")
# Obtener la longitud de la lista de palabras
words_count = len(words_list)

# Salida de información
print(f'La frase tiene {words_count} palabras.')