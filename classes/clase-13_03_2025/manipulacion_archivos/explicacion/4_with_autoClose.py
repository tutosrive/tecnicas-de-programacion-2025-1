# Leer un archivo con 'with'
with open('./manipulacion_archivos/explicacion/data/my_file.txt', 'r') as file:
    content = file.read()
    print(content)
