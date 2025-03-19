"""
Enunciado:
    Lea un archivo de texto y cuente cuántas veces aparece una palabra específica.

Pseudocódigo:
    IMPORTAR DEL ARCHIVO "ejercicio2.py" LA FUNCIÓN "splitter"

    ABRIR ARCHIVO "./manipulacion_cadenas/data/count_words.txt" EN MODO LECTURA
    content_file <- LEER CONTENIDO DEL ARCHIVO
    CERRAR ARCHIVO

    // Se usa la fnción del ejercicio anterior (splitter)
    list_words <- splitter(content_file, " ")

    // Palabra que se buscará en el contenido del archivo
    word <- "math"

    // Contador de veces que aparece la palabra
    word_count <- 0

    // Recorrer cada palabra del contenido del archivo
    PARA i <- 1 HASTA list_words.length() CON PASO 1 HACER
        SI word = list_words[i] THEN
            word_count <- word_count + 1
        FIN SI
    FIN PARA
    ESCRIBIR "La palabra '", word, "' Aparece ", word_count, " veces en el archivo."

Estrategia:
    En primer lugar se planea reutilizar código del ejercicio 2, ya que cumple con el mismo principio,
    buscar una palabra específica, y para ello se reutiliza la función "splitter", la cual nos ayuda a "separar/cortar" el contenido
    del texto (ya que es un String), y nos permitirá obtener una lista de cada palabra que contiene el archivo,
    una vez tenemos la lista de palabras, solo nos queda buscar las coincidencias exactas y aumentar un contador previamente inicializado
    en cero (0)
"""

# Reutilzar código del "ejercicio2.py"
from ejercicio2 import splitter

content_file = ""
with open('./manipulacion_cadenas/data/count_words.txt', 'r', encoding='utf-8') as file:
    content_file = file.read()

# Se usa la fnción del ejercicio anterior (splitter)
# "separar" contenido en una lista de palabras (separadro = " ")
list_words = splitter(content_file, " ")

# Palabra que se buscará en el contenido del archivo
word = "math"
# Contador de veces que aparece la palabra
word_count = 0

# Recorrer cada palabra del contenido del archivo
for w in list_words:
    if word == w:
        word_count += 1

print(f'La palabra "{word}" Aparece {word_count} veces en el archivo.')