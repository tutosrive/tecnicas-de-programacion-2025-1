"""
Enunciado:
    Escriba un programa que cuente cuántas vocales tiene una cadena ingresada por el usuario.

Pseudocódigo:
    ESCRIBIR ("Ingrese una frase: ")
    LEER frase
    vocales_contador <- 0
    vocales <- ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    PARA i <- 1 HASTA length(frase.lower()) CON PASO 1 HACER
        PARA j <- 1 HASTA vocales.length() CON PASO 1 HACER
            SI frase[i] = vocales[j] THEN
                vocales_count++
        FIN PARA
    FIN PARA
    ESCRIBIR("La frase tiene ", vocales_count, " vocales")       

Estrategia: 
    Solicitar al usuario la información requerida, luego, tenemos una lista de vocales con tíldes incluidas
    se recorrerá cada caracter de la frase, y cada caracter será comparado con cada una de las vocales de la lista
"""
# Contador de vocales
vocales_contador: int = 0
# Definición de variables de comparación
vocales: list = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

# Ingreso de información
frase:str = input("Ingrese una frase: ")

# Recorrer cada caracter de la frase ingresada
for char in frase.lower():
    # Recorrer la lista de vocales
    for vocal in vocales:
        # Comparar el caracter actual con cada vocal de la lista
        if char == vocal:
            # Si ambos son iguales, se aumenta el contador
            vocales_contador += 1

# Salida de información
print(f'La frase tiene {vocales_contador} vocales.')