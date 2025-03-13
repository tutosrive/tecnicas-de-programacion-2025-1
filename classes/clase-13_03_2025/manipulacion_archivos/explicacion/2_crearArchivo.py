# Crear y escribir en un archivo de texto
# No requiere librerías adicionales en Python
# En este caso se creará en la ROOT de este proyecto...
with open('my_file.txt', 'w') as file:
    file.write('Hola, este es un archivo de texto')