"""
Concepto:
    En programación, los archivos permiten almacenar datos de forma persistente. Existen operaciones de lectura y escritura en archivos de texto y binarios.
    Ejemplo en pseudocódigo:
        Abrir archivo "datos.txt" en modo escritura
        Escribir en archivo "Hola, este es un archivo de texto."
        Cerrar archivo

        Abrir archivo "datos.txt" en modo lectura
        Leer contenido del archivo y mostrar en pantalla
        Cerrar archivo

        Ejemplo en Python:
            # Escritura en un archivo
            with open("datos.txt", "w") as archivo:
                archivo.write("Hola, este es un archivo de texto.\n")
                archivo.close()

            # Lectura de un archivo
            with open("datos.txt", "r") as archivo:
                contenido = archivo.read()
                print(contenido)
                archivo.close()
"""
# Escritura en un archivo
with open("./manipulacion_datos/explicacion/data/datos.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.close() # Cerrar archivo

# Lectura de un archivo
with open("./manipulacion_datos/explicacion/data/datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    archivo.close() # Cerrar archivo