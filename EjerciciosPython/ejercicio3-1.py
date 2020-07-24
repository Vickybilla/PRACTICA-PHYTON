"""Ejercicio 1: Crear una función que, a partir de un dato de entrada que sea en horas, nos informe cuántos minutos
y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores."""


def minutos_segundos_a_horas(hora_usuario=int(input("Ingrese un valor en horas "))):
    minutos = hora_usuario * 60
    segundos = hora_usuario * 3600
    # return minutos and segundos
    print(f"{hora_usuario} horas ingresadas son " + str(minutos) + " minutos y su valor en segundos es de  " +
          str(segundos))

minutos_segundos_a_horas()
