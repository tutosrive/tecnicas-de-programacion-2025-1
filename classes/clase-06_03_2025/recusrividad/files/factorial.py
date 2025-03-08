def fact(n:int) -> int:
    factorial:int = 0
    # Caso base
    if n in [0,1]:
        factorial = 1
    elif n < 0:
        # Caso de error
        raise ValueError(f"No existe factorial para: {n}")
    else:
        # Caso general
        factorial = n * fact(n - 1)
    return factorial