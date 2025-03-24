"""
Enunciado:
    Filtre de una lista de números solo los que sean pares y almacénelos en otra lista.
"""
# Lista de números generada dinámicamente
numbers: list[int] = [(x * x + 2) for x in range(210)]
print(f'Números => {numbers}', end='\n\n')

# Lista de números pares generada dinámicamente, solo se agregan los que cumplan la condición
even_numbers: list[int] = [even for even in numbers if even % 2 == 0]
print(f'Números pares => {even_numbers}')