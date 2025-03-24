"""
Enunciado:
    Documente un programa que lea nombres desde un archivo y los almacene en una lista.
"""
import csv

def read_file_to_list(file_path: str) -> list:
    """Leer nombres de un archivo CSV

    ## Nota:  
        La función cuenta con el sistema de captura de errores (excepciones) referentes al archivo.

    Args:
        file_path (str): Ruta del archivo del cual se extraerán los nombres

    Returns:
        list: Lista con cada uno de los nombres del archivo especificado
    """
    names: list = []
    try:
        # Intenta abrir el archivo especificado en modo lectura
        with open(file_path, 'r', encoding='utf-8') as file:
            # Se crea un iterador "reader" del archivo CSV
            reader_file = csv.reader(file)
            # Se omite el encabezado del archivo
            next(reader_file)
            # Se accede a cada item del iterador y se agrega a la lista de nombres
            for row in reader_file:
                names.append(row[0])
    except FileNotFoundError:
        print(f"No se encuentra el archivo {file_path}")
    
    return names

# Ruta del archivo CSV
names_file: str = './documentacion_codigo_fuente/data/names.csv'
# Obtener una lista de los nombres registrados en el archivo
names_list:list = read_file_to_list(names_file)
# Salida de información
print(names_list)