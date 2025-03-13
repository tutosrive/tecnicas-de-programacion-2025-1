"""
Concepto:
Documentar el código es importante para su mantenimiento. En Python, se usan comentarios `#` y docstrings `""" """`.
Ejemplo en pseudocódigo:
    // Función que suma dos números
    Funcion Sumar(a, b)
        Retornar a + b
    Fin Funcion

Ejemplo en Python:
    def sumar(a, b):
        '''Esta función suma dos números y devuelve el resultado.'''
        return a + b

print(sumar(3, 5))
"""
def sumar(a:int, b:int) -> int:
    """Esta función suma dos números y devuelve el resultado.

    Args:
        a (int): Número 1
        b (int): Número 2

    Returns:
        int: Suma de número 1 y número 2
    """
    return a + b

print(sumar(12, 5))