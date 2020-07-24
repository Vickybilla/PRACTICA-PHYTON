"""Ejercicio 9: Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito.
 Evaluar si puede realizar una compra de $2500,
si puede indicar cuánto saldo le queda luego de efectuarla.
Si no puede, indicar cuánto dinero le falta para poder realizarla."""

tarjeta_disponible = float(input("Ingrese el monto disponible en su tarjeta de credito  "))
compra = 2500

if tarjeta_disponible >= compra:
    transaccion = tarjeta_disponible - compra
    print("Su disponible luego de la copra sera de " + str(transaccion) + " pesos")
else:
    tarjeta_disponible < compra
    falta = tarjeta_disponible - compra
    print("Para realizar esta operacion le faltan " + str(abs(falta)) + " pesos")
