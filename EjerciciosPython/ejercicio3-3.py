"""Ejercicio 3: Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números,
si los hay, que aparecen en dicho mensaje."""


def numeros_en_mensaje(mensaje):
    lista_numeros = []
    for num in mensaje:
        if num.isdigit():
            lista_numeros.append(num)
    print(lista_numeros)


mensaje = input(" escriba un mensaje ")

print(numeros_en_mensaje(mensaje))
