try:
    # Tratar de abrir el archivo
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError: # Capturar el error
    print('El archivo no existe.')