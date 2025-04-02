def next_permutation(arr):
    n = len(arr)
    k = -1
    # Buscar el índice k tal que arr[k] < arr[k+1]
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            k = i
    # Si k sigue siendo -1, es que no hay más permutaciones
    if k == -1:
        return False

    l = -1
    # Buscar el índice l tal que arr[k] < arr[l]
    for i in range(k + 1, n):
        if arr[k] < arr[i]:
            l = i

    # Intercambiar arr[k] con arr[l]
    arr[k], arr[l] = arr[l], arr[k]

    # Invertir el subarreglo de arr[k+1] hasta arr[n-1]
    inicio = k + 1
    fin = n - 1
    while inicio < fin:
        arr[inicio], arr[fin] = arr[fin], arr[inicio]
        inicio += 1
        fin -= 1

    return True

def imprimir_vector(arr):
    # Imprime cada número del vector separado por un espacio
    for num in arr:
        print(num, end=" ")
    print()  # Salto de línea

def generar_permutaciones(n):
    # Inicializar el vector con la secuencia 0, 1, 2, ..., n-1
    permutation = [i for i in range(n)]
    # Imprimir la permutación inicial
    imprimir_vector(permutation)
    
    # Generar todas las permutaciones usando fuerza bruta
    while next_permutation(permutation):
        imprimir_vector(permutation)

n = 4  # Puedes cambiar el tamaño del tablero aquí
generar_permutaciones(n)
