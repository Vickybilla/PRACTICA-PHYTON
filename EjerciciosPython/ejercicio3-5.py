"""Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números,
False si hay al menos uno de los parámetros ingresados que no es un número,
y None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla."""


def boolean_item(*param):
    lista_mensaje = []
    for item in param:
        if type(item) == int or type(item) == float or type(item) == complex:
            lista_mensaje.append(item)
    if len(param) == len(lista_mensaje):
        return True
    elif len(lista_mensaje) != 0:
        return False
    else:
        return None


print((boolean_item(1, 35)))
