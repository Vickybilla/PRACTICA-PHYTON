"""Ejercicio 9: Crear un diccionario con 10 estudiantes y sus respectivas notas. Luego crear una función que nos
 informe los estudiantes aprobados (nota >= 7), los estudiantes desaprobados (4 <= nota < 7) y
  los estudiantes aplazados (0 <= nota < 4)."""

les_alumnes = {}

print("Ingrese el nombre de cada estudiante y su nota correspondiente")
for i in range(10):
    nombre = input("Nombre: ")
    nota = int(input("Nota: "))
    les_alumnes[nombre] = nota


def informe_notas():
    aprobados = {}
    desaprobados = {}
    aplazados = {}
    for nombre_alumne, nota_alumne in les_alumnes.items():
        if nota_alumne >= 7:
            aprobados[nombre_alumne] = nota_alumne
        elif 4 <= nota_alumne < 7:
            desaprobados[nombre_alumne] = nota_alumne
        elif 0 <= nota_alumne < 4:
            aplazados[nombre_alumne] = nota_alumne
        else:
            print("La nota debe estar entre 0 y 10.") #Agregado del código de Maga
    if len(aprobados) != 0:
        print(f"Los aprobados son: {aprobados}")
    if len(desaprobados) != 0:
        print(f"Los desaprobados son: {desaprobados}")
    if len(aplazados) != 0:
        print(f"Los aplazados son: {aplazados}")


informe_notas()
