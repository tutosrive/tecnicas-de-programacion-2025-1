"""
Enunciado:
    Escriba comentarios en un programa que convierta temperaturas de Celsius a Fahrenheit.
"""
def celcius_to_farenheit(grades_celcius: float) -> float:
    """Convertir grados **Celcius** a **Farenheit** mediante la siguiente fórmula (**°F = (°C × 9/5) + 32**)

    Args:
        grades_celcius (float): Grados Celcius que se convertirán a Farenheit

    Returns:
        float: Grados Farenheit "redondeados" a tres decimales, obtenidos por medio del cálculo de la fórmula
    """
    # Realizar cálculo mediante fórmula
    farenheit: float = (grades_celcius * (9/5)) + 32
    return float(f'{farenheit:.3f}')

# Grados Celcius
celcius: float = 55.32

# Obtener grados Farenheit a partir de los grado Celcius
farenheit: float = celcius_to_farenheit(celcius)

print(farenheit)