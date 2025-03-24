"""
Enunciado:
    Documente una función que ordene una lista de números de menor a mayor.
"""

def sorting_ascendent(x: list) -> None:
    """Ordenar lista de forma ascendente mediante el algoritmo "**Bubble Sort**" (Ordenamiento Burbuja)

    Args:
        x (list): Lista que se desea ordenar, esta lista debe ser **estrictamente** de tipo numérico (**float** ó **int**)
    """
    # Ciclo en rango de longitud de lista
    for i in range(len(x)):
        # Ciclo usado para comparar uno a uno el par de número adyacentes
        for j in range(len(x) - i - 1):
            # Verificar si el valor de la "izquierda" [j] es mayor al de la "derecha"
            if x[j] > x[j + 1]:
                # Copiar valor que será sobreescrito
                centinel = x[j + 1]
                # Cambiar posiciones
                x[j + 1], x[j] = x[j], centinel

vector = [0,2,4,1,6,3,4,58,0,2]
sorting_ascendent(vector)
print(vector)