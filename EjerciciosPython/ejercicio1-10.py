"""Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y
 luego elimine las vocales y nos devuelva una
lista sin las vocales, sin modificar la original."""


abcCompleto=("A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

listaSinVocales=[]

vocales=("AEIOU")


for letra in abcCompleto:
    if letra not in vocales:
        listaSinVocales.append(letra)
print(listaSinVocales)
