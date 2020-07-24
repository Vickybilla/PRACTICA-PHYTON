"""Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números,
 si el primero es menor que el segundo imprimir la resta entre el segundo y el primero,
si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir su producto."""

#numeros_usuario=input("Ingresar ")
primerNumero= int(input("Ingresa un numero :  "))
segundoNumero= int (input( "Ingresa un segundo numero :  "))

if primerNumero < segundoNumero:
    print(segundoNumero-primerNumero)
elif primerNumero > segundoNumero:
    print(primerNumero + segundoNumero)
else:
    primerNumero == segundoNumero
    print(primerNumero*segundoNumero)