"""
    Lenguaje ficticio "ante" - "ente" en una lista de palabras
    1. Almacena la lista de palabras
    2. Para cada palabra en la lista:
        a. Añade guión "-"
        b. Si la primera letra es vocal:
            i. Añade "ante"
        c. Si no:
            i. Añade la primera letra
            ii. Añade "ente"
            iii. Elimina la primera letra
"""

def add_to_words(__words: str = None):
    # Pedir una "frase" al usuario y "cortar" la frase en cada espacio
    words = __words if __words is not None else input("Ingrese una frase (Cada palabra separada por un espacio): ")
    words = words.split(' ')

    # Se usa "for común" porque se requiere paso por referencia...
    for i in range(len(words)):
        words[i] += "-"
        first_char = words[i][0] # Primer carácter de cada palabra
        if first_char.lower() in ['a', 'e', 'i', 'o', 'u']:
            words[i] += "ante"
        else:
            words[i] += first_char
            words[i] += "ente"
            # Reemplaza con un "vacío" (Sólo la primer coincidencia)
            words[i] = words[i].replace(first_char, '', 1)
        return words