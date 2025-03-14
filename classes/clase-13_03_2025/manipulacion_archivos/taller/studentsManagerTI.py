import files.generators as gener
import files.file_manager as file_man
import files.calculation as calc

# Ruta de acceso del directorio "data"
data_path = "./taller/data"
student_file = f'{data_path}/students.csv'
notes_file = f'{data_path}/notes.csv'

# Encabezados de archivos
file_man.write_csv(student_file, True, ["identification", "name", "lastname", "age", "code_id", "email"])
file_man.write_csv(notes_file, True, ["period1", "period2", "period3", "final_note"])

for i in range(25):
    # Entrada de datos de usuario (nombre, edad, e.t.c.)
    name = input("Ingrese su nombre: ")
    lastname = input("Ingrese su apellido: ")
    age = int(input("Ingrese su edad (solo el número): "))
    identification = input("Ingrese su número de identificación: ")
    code_id = input("Ingrese su código estudiantil: ")
    # Generar email para el estudiante actual
    email = gener.generate_email(name, lastname, code_id)
    # Escribir los datos del estudiante en su archivo correspondiente
    file_man.write_csv(student_file, True, [name, age, identification, code_id, email], 'a')

    # Notas
    data = []
    # Obtener las notas de los 3 peridos/cortes
    for i in range(3):
        note = float(input(f"Ingrese la nota del periodo/corte {i + 1}: "))
        data.append(note)
    # Calcular notas finales de cada periodo/recorte
    calc.calc_all_percent_note(data)
    # Calcular nota final del estudiante
    final_note_student = calc.calc_final_note(data)[1]
    # Agregar nota final del estudiante
    data.append(final_note_student)
    # Escribir notas finales de cada periodo/recorte y la nota final del estudiante
    file_man.write_csv(notes_file, True, data, 'a')

# Lectura de todas las notas
all_notes = file_man.read_csv(notes_file)[1]
students_list = file_man.read_csv(student_file)[1]

# Promedio general del grupo
general_prom:float = calc.calc_general_prom(all_notes)
print(f'Promedio general del grupo de estudiantes: {general_prom}')