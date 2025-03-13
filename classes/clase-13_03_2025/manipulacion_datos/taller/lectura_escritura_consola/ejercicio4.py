"""
Enunciado:
    Escriba un programa que pregunte al usuario tres calificaciones y calcule su promedio.

Pseudocódigo:
    cal <- 0
    Para i <- 1 Hasta 3 Con Paso 1 Hacer
        ESCRIBIR ("Ingrese la calificación ", i , " : ")
        LEER nota
        cal <- cal + nota
	Fin Para
    promedio <- cal/3
    ESCRIBIR ("Su prmedio es: ", promedio)

Estrategia:
    Se hizo uso de un ciclo for para solicitar información al usuario (calificaiones) y luego calcular su promedio
"""
# Variable de calificaciones
cal:float = 0.0
# Solicitar calificaciones con ayuda del for
for i in range(3):
    # Sumar las calificaciones
    cal += float(input(f"Ingrese la calificación {i + 1}: "))

# Calcular promedio
promedio:float = cal / 3
# Salida de información
print(f"Su promedio es: {promedio}")