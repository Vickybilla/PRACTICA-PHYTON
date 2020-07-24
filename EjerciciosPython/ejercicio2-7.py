"""Ejercicio 7: Crear un diccionario con 5 estudiantes y sus respectivas notas.
 Imprimir por pantalla los alumnos que aprobaron y su nota (no en forma de diccionario, si no con nombre : nota).
 Tener en cuenta que para aprobar el alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10."""

dic_estudiantes_notas = {
    "Leonardo": 10,
    "Agustina": 8,
    "Victoria": 7,
    "Violeta": 5,
    "Bautista": 4
}
alumnos_aprobados = {}

for student, note in dic_estudiantes_notas.items():
    if 7 <= note <= 10:
        alumnos_aprobados[student] = note
        print(str(student) + ":" + str(note))
