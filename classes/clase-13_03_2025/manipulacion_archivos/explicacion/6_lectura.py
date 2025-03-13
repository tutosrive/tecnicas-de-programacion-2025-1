"""
read(): Lee todo el contenido.
readline(): Lee una línea a la vez.
readlines(): Lee todas las líneas y las guarda en una lista.
"""
file_path:str = './manipulacion_archivos/explicacion/data/products.txt'
# Leer todo el contenido
with open(file_path, 'r') as file:
    content = file.read()
    print("Contenido completo:\n", content)

# Leer línea por línea
with open(file_path, 'r') as file:
    line = file.readline()
    line_count = 1
    while line:
        print(f"Línea {line_count}:", line.strip())
        line = file.readline()
        line_count += 1

# Leer todas las líneas en una lista
with open(file_path, 'r') as file:
    lines = file.readlines()
    print("Lista de líneas:", lines)