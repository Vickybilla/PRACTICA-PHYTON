"""Ejercicio 6: Escribir un programa que seleccione una operación de cuatro operaciones numéricas disponibles,
una vez seleccionada la operación, introducir dos números y ejecutar la operación."""

operacion = input("""por favor indicar operacion entre: suma,resta,division, o multiplicacion""")
num1 = int(input("Ingresa un numero :  "))
num2 = int(input("Ingresa un segundo numero :  "))

if operacion == "suma":
   resultado = num1 + num2
   print(resultado)
elif operacion == "resta":
    resultado = num1 - num2
    print(resultado)
elif operacion == "division":
    resultado = num1 / num2
    print(resultado)
else:
    operacion == "multiplicacion"
    resultado = num1 * num2
    print(resultado)
