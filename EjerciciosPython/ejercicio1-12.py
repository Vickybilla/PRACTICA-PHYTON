"""Ejercicio 12: Crear un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar."""
from _ast import operator

vector1= [1,2,3]
vector2=[-1,0,2]
listaescalar=[]



for x in range(len(vector1)):
    listaescalar.append((vector1[x]*vector2[x]))
print(listaescalar)







"""for x in vector1:
    v1=vector1[v]
    v2=vector2[v]
    listaescalar.append(v1*v2)
print(listaescalar)
for x in vector1:
   for y in vector2:
    listaescalar.append(x**y)
print(listaescalar)"""



