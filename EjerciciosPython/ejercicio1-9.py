"""Ejercicio 9: Crear un programa que pregunte al usuario 5 números enteros
 y devuelva una lista con ellos."""

listaUsuario= []
for x in range(5):
    numero=int(input("Ingrese un numero entero: "))
    listaUsuario.append(numero)
print(listaUsuario)
