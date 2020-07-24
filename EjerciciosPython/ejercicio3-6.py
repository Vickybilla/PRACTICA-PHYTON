"""Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title.
Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"""


# no pasa a title, ver pór qué

def mensaje_title(mje):
    if mje.istitle():
        print(f"El mensaje  está en modo title: {mje}")
    else:
        mje.title()
        print(mje.title())


mensaje_title("me estoy poniendo al día con python")
