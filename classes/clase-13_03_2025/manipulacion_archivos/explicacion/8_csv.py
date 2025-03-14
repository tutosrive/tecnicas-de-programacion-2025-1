import csv  # Importar la librería csv

data_path = './explicacion/data/data.csv'

# Escribir en un archivo CSV
with open(data_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Escribir por filas
    writer.writerow(['Nombre', 'Edad', 'Ciudad'])
    writer.writerow(['Alice', 28, 'New York'])
    writer.writerow(['Bob', 34, 'Los Angeles'])

# Leer desde un archivo CSV
with open(data_path, 'r') as csvfile:
    reader = csv.reader(csvfile) # Lectura por filas
    # Leer cada fila
    for row in reader:
        print(row)
