import os  # Importar la librería os

# Verificar si un archivo existe
if os.path.exists('my_file.txt'):
    print("1. El archivo existe.")
else:
    print("1. El archivo no existe.")

# Archivo existente
if os.path.exists('./explicacion/data/my_file.txt'):
    print("2. El archivo existe.")
else:
    print("2. El archivo no existe.")