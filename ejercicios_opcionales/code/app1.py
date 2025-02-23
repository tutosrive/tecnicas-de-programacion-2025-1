"""
    Lenguaje ficticio "ante" - "ente" en solo una palabra
    1. Añade "-"
    2. Almacena la primera letra
    3. Si la primera letra es vocal:
        a. Añade "ante"
    4. Si no:
        a. Añade la primera letra
        b. Añade "ente"
        c. Elimina la primera letra
"""

def add_to_word(__word:str = None) -> str:
    word =  __word if __word is not None else input("Ingrese una palabra: ")
    # 1
    word += "-"
    # 2
    # Caracter en posición cero
    first_char = word[0]

    # Validar si se encuentra en la lista de vocales
    if first_char in ['a', 'e', 'i', 'o', 'u']:
        word += "ante"
    else:
        word += first_char
        word += "ente"
        # Reemplaza con un "vacío" (Sólo la primer coincidencia)
        word = word.replace(first_char, '', 1)
    return word