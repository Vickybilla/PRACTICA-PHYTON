"""Ejercicio 7: Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs y
  su pago por hora es de 400 pesos. Devolver el sueldo por pantalla."""


valorHoraTrabajada= 400
horasPorDia=8
dias_trabajados= int(input(" Ingresar la cantidad de dias trabajados "))
sueldo_bruto=dias_trabajados*(horasPorDia*valorHoraTrabajada)
print("El sueldo bruto es " +str(sueldo_bruto))


