import csv

def write_csv(file_path:str, single_row:bool = False, data:list = None, mode:str = 'w') -> None:
    """Escribir datos en un archivo CSV

    Args:
        file_path (str): Ruta del archivo CSV
        mode (str, optional): Modo de apertura (solo se admite 'w' o 'a'). Por defecto es 'w'.
        single_row (bool, optional): ¿Se escribirá solo una fila?. Por defecto es False.
        data (list, optional): Datos que se escribirán en el CSV. por defecto es None.

    Raises: 
        TypeError: No se enviaron datos (se captura dentro de este procedimiento) 
        ValueError: Modo de apertura erróneo (se captura dentro de este procedimiento)
    """
    try:
        # No se enviaron datos para escribir
        if data == None:
            # Lanzar excepción (Se captura en línea)
            raise TypeError
        elif mode not in ['w', 'a']:
            # Modo de apertura erróneo
            raise ValueError
        else:
            # Tratar de abir archivo en el modo establecido
            with open(file_path, mode, encoding="utf-8", newline='') as file:
                csv_writer = csv.writer(file)
                if single_row:
                    csv_writer.writerow(data)
                else:
                    csv_writer.writerows(data)
    except FileNotFoundError:
        print(f"No se encontró el archivo {file_path}")
    except TypeError:
        print("Debe enviar los datos que desea escribir en el archivo")
    except ValueError:
        print(f'No se admite el modo "{mode}" de apertura de archivo en este procedimiento')

def read_csv(file_path:str) -> tuple:
    """Leer archivo CSV

    Args:
        file_path (str): Ruta de archivo CSV

    Returns:
        tuple: Tupla con dos posiciones:
            - Primera posición indica si se realizó la operación con un valor booleano
            - Segunda posición son los datos recuperados del archivo (None en posición 0 si hay error, es decir si primera posición es False)
    """
    try:
        # Tratar de abir archivo en el modo establecido
        with open(file_path, 'r', encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # Saltarse encabezado
            # Se crea una lista del iterador del READER, porque se cierra el archivo automáticamente
            # por tanto la referencia del READER se elimina
            return True, list(csv_reader)          
    except FileNotFoundError:
        print(f"No se encontró el archivo {file_path}")
        return False, [None]