"""Ejercicio 10: Utilizar el método range() para recorrer el iterable
e imprimir solo los números impartes entre 1 y 40 inclusive."""

for x in range(1, 41):
    if x % 2 != 0:
        print(x)

lista_impares = []
for num in range(1, 41):
    if num % 2 != 0:
        lista_impares.append(num)
print(lista_impares)
