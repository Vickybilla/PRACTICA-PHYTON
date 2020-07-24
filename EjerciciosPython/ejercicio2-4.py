"""Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros,
ordenarlos de manera creciente e imprimirlos por pantalla."""

numeros_usuario=[]
for x in range(6):
    numero=int(input("Ingrese un numero entero: "))
    numeros_usuario.append(numero)
numeros_usuario.sort()
print(numeros_usuario)