"""Ejercicio 10: Crear una función decoradora para una función matemática cualquiera."""


def funcion_deco_math(funcion_mate):
    def operacion_mate(*args, **kwargs):
        print("realizaremos una operación matemática")
        funcion_mate(*args, **kwargs)
        print("done")

    return operacion_mate


@funcion_deco_math
def multiplo(num1, num2):
    print(num1 * num2)


@funcion_deco_math
def potencia(base, exponente):
    print(pow(base, exponente))

multiplo(4,5)

potencia(base=2, exponente=6)

