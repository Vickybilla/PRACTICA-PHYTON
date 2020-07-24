"""Ejercicio 2: Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor.
 Si al menos hay 3 números mayores a 100, imprimir esos números, si no,
 imprimir los números menores a 50 que formen parte de la lista."""

lista_num= [2,4,6,7,23,977,6.0,3,66,8965]

lista_num.sort(reverse=False)
print("El numero mayor es  "+ str(lista_num[-1]))
print("El numero mayor es " + str(lista_num[0]))
lista_mayores=[]
lista_menores=[]
for x in lista_num:
    if x > 100:
        lista_mayores.append(x)
    else:
        x < 50
        lista_menores.append(x)

if len(lista_mayores) > 3:
    print(lista_mayores)
else:
    print(lista_menores)
