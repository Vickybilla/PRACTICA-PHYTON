"""Ejercicio 1: Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene
más de 100 caracteres imprimirlo por pantalla, si tiene entre 50 y 100 caracteres imprimirlo al revés,
si no se cumple ninguna de las opciones anteriores,
por pantalla devolver un mensaje que diga "su mensaje es demasiado corto"."""

mensaje_de_usuario = input("Ingrese un mensaje cualquiera ")
# mensaje_de_usuario.count(len(mensaje_de_usuario))

"""if len(mensaje_de_usuario) > 100:
    print(mensaje_de_usuario)
elif 50 < len(mensaje_de_usuario) < 100:
    print(mensaje_de_usuario[::-1])
else:
    0 < len(mensaje_de_usuario) <50
    print("el mensaje es demasiado corto ")"""
#solucion
if len(mensaje_de_usuario) < 50:
    print("el mensaje es demasiado corto ")
elif 50 < len(mensaje_de_usuario) < 100:
    print(mensaje_de_usuario[::-1])
else:
    len(mensaje_de_usuario) > 100
    print(mensaje_de_usuario)



