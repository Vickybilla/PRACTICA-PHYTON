"""Ejercicio 2: Crear una función que devuelva una lista con todos los
 números pares del 0 al 100 inclusive. Imprimir esa lista por pantalla."""


def numeros_pares():
    lista_pares = []
    for num in range(101):
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares

print(numeros_pares())

