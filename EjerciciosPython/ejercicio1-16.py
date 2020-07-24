"""Ejercicio 16: Crear un programa que cree un diccionario vacío y
lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo,
teléfono, correo electrónico, etc.) que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""



info_usuario={}

claves_usuario=["nombre","edad","sexo","telefono","correo electronico","domicilio","color favorito"]

for clave in claves_usuario:
    valor= input("Ingrese su " + str(clave))
    info_usuario[clave] = valor
    print(info_usuario)



"""agregar = 'Si'
while agregar=='Si':
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    info_usuario[clave] = valor
    print(info_usuario)
    agregar= input('¿Quieres añadir más información (Si/No)? ')""" #esto anda pero pregunta mucho





