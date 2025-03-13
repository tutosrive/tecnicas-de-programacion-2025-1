"""
Enunciado:
    Escriba un programa que lea dos números enteros desde la consola y muestre su suma, resta, multiplicación y división.

    Pseudocódigo:
    ESCRIBIR ("Imgrese su primer numero")
    LEER numero1
    ESCRIBIR ("ingrese su segundo numero")
    LEER numero2
    ESCRIBIR ("División: ", numero1/numero2)
    ESCRBIR ("SUMA: ", numero1+numero2)
    ESCRBIR ("RESTA: ", numero1-numero2)
    ESCRBIR ("MULTIPLICACION: ", numero1*numero2)

    ESTRATEGIA:
    solicitar dos numeros al usuario por consola y aplicar las operaciones correspondientes.
"""
# Ingreso de la información
numero1:int = int(input("Ingrese su primer numero: "))
numero2:int = int(input("ingrese su segundo numero: "))

# Operaciones correspondientes
suma:int = numero1+numero2
resta:int = numero1-numero2
division:float = numero1/numero2
multiplicacion:int = numero1*numero2

# Salida de información
print("SUMA: ", suma)
print("RESTA: ", resta)
print("División: ", division)
print("MULTIPLICACION: ", multiplicacion)