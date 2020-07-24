"""Ejercicio 14: Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono
 y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.
"""

diccionario_datos={}
nombre= input("Ingrese su nombre ")
diccionario_datos["nombre"]=nombre
edad= int(input("Ingrese su edad  "))
diccionario_datos["edad"]=edad
domic= input("Ingrese su domicilio  ")
diccionario_datos["domicilio"]=domic
tel= input("Ingrese su telefono  ")
diccionario_datos["telefono"]=tel

print("los datos del usuario son "+ str(diccionario_datos))




