"""
Enunciado:
    Escriba una función que calcule la potencia de un número y documente su propósito con docstrings.
"""
def pow_to(base: float, exponent: int) -> float:
    """"Elevar" un número a la potencia indicada

    Args:
        base (float): Número que requiere potenciar
        exponent (int): Potencia a la cual se elevará la base

    Returns:
        float: Se retorna la base (número) potenciada al exponente indicado
    """
    __pow = base ** exponent
    return __pow

print(pow_to(2, 5)) # 32