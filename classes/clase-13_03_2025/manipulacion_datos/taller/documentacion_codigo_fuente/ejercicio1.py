"""
Enunciado:
    Agregue comentarios adecuados a un programa que calcule el área de un triángulo.

Estrategia:
    Los comentarios son una breve descripción de lo que una instrucción hace, en 
    funciones y clases, los comentarios pasan a ser una descripción detallada de lo que
    se espera retorne una función o qué parámetros se deben enviar y de que tipo
"""

def area_triangle(base: float, height: float) -> float:
    """Calcular el área de un triángulo por medio de su base y altura

    Args:
        base (float): Medida de la base del triángulo (número decimal)
        height (float): Medida de la altura del triángulo (número decimal)

    Returns:
        float: Retorna el área calculada por medio de su base y altura
    """
    area: float = (base * height) / 2
    return area