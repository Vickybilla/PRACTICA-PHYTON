# creacion de funcion decoradora

def funcion_deco(funcion_parametro):
    def funcion_interna(*args):  # agrego un valor indeterminado de parametros
        print("vamos a realizar un cálculo: ")
        funcion_parametro(*args)  # y acá tambien sino va a dar error
        print(" hemos terminado el calculo ")

    return funcion_interna  # aQUI SIGUE SIN PONER PARENTESIS NI PARAMETRO!S


@funcion_deco  # asigno a la funcion suma como funcion parametro
def suma(a, b, c):
    print(a + b + c)


suma(1, 2, 3)

"""def ladrido(funcion_original):
    def guauguau():
        funcion_original()
        print("El perro hace guau guau")
    return guauguau

@ladrido
def perro():
    print("Adopté un perrito la semana pasada")
perro()

def gato():
    print("adopté un gatito")

gato()
"""
