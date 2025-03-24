"""
Enunciado:
    Extraiga el nombre de usuario de una dirección de correo electrónico dada (antes de la @).

Pseudocódigo:
    IMPORTAR DEL ARCHIVO "ejercicio2.py" LA FUNCIÓN "splitter"
    // Ingreso de información
    ESCRIBIR "Ingrese su E-Mail: "
    LEER email

    // Reutilizar función del "ejercicio2"
    // Se separa el correo en 2 partes, el nombre de usuraio y el dominio (userName, empresa.com)
    email_splitted <- splitter(email, '@')
    user_name <- email_splitted[0]

    ESCRIBIR "Su nombre de usuario es: ", user_name

Estrategia:
    Se plateó la idea de separar (reutilizando la función "splitter" del ejercicio2) el correo por un caracter único e irrepetible 
    dentro de una dirección de correo electrónico el @, con esto, podemos obtener fácilmente el nombre de usuario que siempre estará 
    en la primera posición.
"""

# Reutilizar la función "splitter" del ejercicio2
from ejercicio2 import splitter

# Ingreso de información
email: str = input("Ingrese su E-Mail: ")

# Reutilizar función del "ejercicio2"
# Se separa el correo en 2 partes, el nombre de usuraio y el dominio (userName, empresa.com)
email_splitted: list = splitter(email, '@')
# Obtener la posición cero
user_name: str = email_splitted[0]

print(f'Su nombre de usuario es:  {user_name}')