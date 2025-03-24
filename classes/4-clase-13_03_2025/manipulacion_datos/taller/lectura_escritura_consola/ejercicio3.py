"""
Enunciado:
    Pida al usuario una frase y cuente cuántas palabras tiene utilizando `split()`.

Pseudocódigo:
    ESCRBIR ("Ingrese una frase: ")
    LEER frase
    frase_separada <- SPLIT(frase, " ")
    cantidad_palabras <- LENGTH(frase_separada)
    ESCRIBIR "Tiene ", cantidad_palabras, " palabras"

Estrategia:
    Solicitar la frase al usuario, dividirla/cortarla por medio de los espacios y se toma la longitud
    de la lista de palabras que nos retorna 'SPLIT()'
"""
frase:str = input("Ingrese una frase: ")
# Se infiere que el usuario ingresa una frase SIN espacios iniciales ni finales
frase_separada:list = frase.split(" ")
cantidad_palabras:int = len(frase_separada)
print(f"Tiene {cantidad_palabras} palabras")