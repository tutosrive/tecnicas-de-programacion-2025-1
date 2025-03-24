"""
Concepto:
    Las cadenas son secuencias de caracteres y se pueden manipular con diversas funciones, como concatenación, búsqueda y reemplazo.

Ejemplo en pseudocódigo:
    cadena <- "Hola Mundo"
    cadena <- Reemplazar(cadena, "Mundo", "Python")
    Escribir "Nueva cadena: " + cadena

Otras operaciones con cadenas:
- split(): Divide una cadena en una lista de subcadenas basadas en un delimitador.
- substring(slice): Extrae una parte de la cadena.
- strip(): Elimina espacios en blanco al inicio y al final.

texto = "  Python es genial  "
print(texto.strip())  # "Python es genial"

palabras = "uno,dos,tres".split(",")
print(palabras)  # ['uno', 'dos', 'tres']

subcadena = texto[2:8]
print(subcadena)  # "Python"
"""

cadena = "Hola Mundo"
cadena = cadena.replace("Mundo", "Python")
print("Nueva cadena:", cadena)

# Reemplazar coincidencias
saludo = "Bienvenido a la clase"
saludo = saludo.replace("la clase", "el curso")
print("Nuevo saludo:", saludo)

# Cortar cadenas por medio de un limitador
cortar_cadena = "Saludos, desde técnicas"
cortar_cadena = cortar_cadena.split(",")
print(cortar_cadena)

# Extraer una parte de la cadena
extraer = "Clase de técnicas de programación"
extraer = extraer[9:17] # Debe ser "técnicas"
print(extraer)

# Eliminar espacios al princio
eliminar_espacios = "      Hola aquí,     saludos!       "
eliminar_espacios = eliminar_espacios.strip()
print(eliminar_espacios)