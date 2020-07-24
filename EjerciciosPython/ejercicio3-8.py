"""Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km,
en un viaje ida y vuelta MdP-Bue si la distancia es de 400km. Luego crear una función que, a partir de esos datos,
devuelva cuánto significa eso en pesos si el litro de nafta está 60$."""


def litros_nafta():
    litros_cada_100k = 2
    km = 100
    distancia_one_way = 400
    litros_consumidos = litros_cada_100k * (distancia_one_way * 2) / km
    return litros_consumidos


def costo_en_pesos(consumo):
    precio_litro = 60
    gasto_total = precio_litro * consumo
    return gasto_total


print(litros_nafta())
print(costo_en_pesos(litros_nafta()))
