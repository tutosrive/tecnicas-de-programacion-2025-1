# Ruta RELATIVA del archivo
file_path:str = "./explicacion/data/products.txt"

# Crear archivo y escribir
file = open(file_path, "w")
# Agregar información (con salto de línea)
file.write("Computador HP 3000\n")

# Abrir archivo en modo de "lectura"
file = open(file_path, "r")
# Leer información del archivo
info:str = file.read()
# Imprimir información
print(f"Información: {info}")

# Nuevamente abrir archivo en modo "agregar/append"
file = open(file_path, "a")
# Agregar información sin sobreescribirla
file.write("Mac Book 4\n")
numbers = [i for i in range(10)]
file.write(f"Números: {str(numbers)}")


# Abrir archivo en modo de "lectura"
file = open(file_path, "r")
# Leer información del archivo
info:str = file.read()
# Imprimir información
print(f"Información nueva: {info}")
file.close()