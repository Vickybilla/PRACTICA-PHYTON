"""Ejercicio 13: Crear un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte
al usuario por una divisa y muestre su símbolo o un mensaje de aviso si
la divisa no está en el diccionario."""

diccionarioDivisas = {
    "Euro": "€",
    "Dollar": "$",
    "Yen": "¥"
}
#divisa=input("Ingrese divisa para mostrar su simbolo ")

"""print(diccionarioDivisas.get(divisa.title(), "La divisa no está en el diccionario."))""" #este codigo funciona

"""for moneda, simbolo in diccionarioDivisas.items():
    if moneda in divisa:
        print(diccionarioDivisas.get(moneda.title()))
else :print("la divisa no esta en el diccionario")"""

for moneda, simbolo in diccionarioDivisas.items():
  # while True:
    divisa=input("Ingrese divisa para mostrar su simbolo ")
    if moneda == divisa:
        print(diccionarioDivisas.get(moneda.title()))
       # break
    else:
        print("la divisa no esta en el diccionario")
        #revisar que no sea alto loop

