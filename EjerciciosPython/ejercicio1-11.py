"""Ejercicio 11: Crear una lista con varios números, luego ordenarlos de manera creciente y
devolver por pantalla la lista ordenada y cuál es el menor y cuál el mayor."""

listaNumeros=[2,4,6,7.8,9,90,5.2]
listaOrdenada=[]

listaNumeros.sort(reverse=False)
print(listaNumeros)
print(min(listaNumeros))
print(max(listaNumeros))
