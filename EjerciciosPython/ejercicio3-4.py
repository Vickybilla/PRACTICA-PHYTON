"""Ejercicio 4: Crear una función que, a partir de 4 números,
 devuelva el mayor producto de dos de ellos. Imprimir resultado por pantalla."""


def mayor_producto():
    num_list = []
    for x in range(4):
        num = int(input("ingrese un numero"))
        num_list.append(num)
    num_list.sort()
    mayor_producto = num_list[-2] * num_list[-1]
    print(mayor_producto)

#codigo de maga quitando el 0 de la lista
"""def prod_mayor():
    lista_numeros = []
    for i in range(4):
        num = int(input("Ingrese un número: "))
        lista_numeros.append(num)
    lista_numeros.sort()
    for numero in lista_numeros:
        if numero == 0:
            lista_numeros.pop(numero)
            mayor_prod = lista_numeros[-2] * lista_numeros[-1]
        else:
            mayor_prod = lista_numeros[-2] * lista_numeros[-1]
    print(mayor_prod)
"""
mayor_producto()