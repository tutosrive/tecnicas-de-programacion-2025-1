"""
Escriba un programa que solicite al usuario su nombre y edad, y luego imprima un mensaje que diga "Hola [nombre], tienes [edad] años".
"""

"""
Estrategia:
    Solicitar por medio de la consola los datos requeridos al usuario (nombre, edad)

Pseudocódigo:
    DEFINIR nombre COMO CARACTER
    DEFINIR edad COMO ENTERO

    ESCRIBIR "Ingrese su nombre: "
    LEER nombre

    ESCRIBIR "Ingrese su edad: "
    LEER edad

    ESCRIBIR "Hola ", nombre, ", tienes ", edad, " años"
"""
# Pedir nombre al usuario
nombre=input("Inrese su nombre: ")
# Pedir edad al usuario
Edad=input("Inrese su edad: ")
# Imprimir información
print("Hola " + nombre + ", tienes ", Edad, " años")