"""Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no. En caso de que lo sea devolver por pantalla
 "La palabra es un palíndromo", en caso contrario, devolver "La palabra no es un palíndromo"."""


def palindroword(palabra):
    if str(palabra) == str(palabra)[::-1]:
        print("La palabra es un palíndromo")
    else:
     print("La palabra no es un palíndromo")


palindroword("ojo")