"""
Enunciado:
     Solicite al usuario su año de nacimiento y calcule su edad actual.

Pseudocódigo:
    ESCRIBIR ("Ingrese su año de nacimiento")
    LEER nacimiento
    ESCRIBIR ("Ingrese el año actual")
    LEER actualYear
    SI nacimiento >= actualYear THEN
        ESCRIBIR("Datos incorrectos (el año de nacimiento no puede ser mayor/igual al actual)")
    SINO
        edad <- actualYear - nacimiento
        ESCRIBIR("Su edad es :", edad)
    FINSI

Estrategia:
    Solicitamos al usuario su año de nacimiento y el años actual, para así hallar la diferencia entre los dos años
    y obtener su edad
"""
# Solicitud de información
nacimiento:int = int(input("Ingrese su año de nacimiento: "))
actualYear:int = int(input("Ingrese el año actual: "))

# Validar si la información dada es correcta
if nacimiento >= actualYear:
    print("Datos incorrectos (el año de nacimiento no puede ser mayor/igual al actual)")
else:
    # Procesacimiento de la información
    edad:int = actualYear - nacimiento
    strYear:str = "años" if edad > 1 else "año" # Operador ternario para edad plural y singular
    # Salida de información
    print(f"Su edad es : {edad} {strYear}")