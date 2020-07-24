#clases y objetos

"""class Perro:
    raza = "labrador"
    edad = "5 años"
    color = "chocolate"
    ladra = False


    #comportamientos

    def ladrar(self, ladrido):
        global ladra
        ladra = ladrido
casla = Perro() #instanciando la clase perro
print(casla.raza) #Nomenclatura del punto
casla.ladrar """

class Cancion : #palabra reservada class para crear una clase

    def __init__(self, letra): #constructor para indicar propiedades iniciales de la clase
        self.letra = letra

    def cantar(self):
        for linea in self.letra:
            print(linea)
#Instancio la clase: creo un objoto perteneciente a ella :lleva un parámetro
feliz_cumpleanios = Cancion(["Que los cumplas felis!,"
                             "Que los cumplas feliz ",
                             "Quwe los cumplas fulanito",
                             "Que los cumplas feliz"])
#llamo al método perteneciente al objeto
feliz_cumpleanios.cantar()
#creo otro objeto

musica_ligera = Cancion(["De aquel amor de musica ligera",
                         "Nada nos libra... nada más queda"])

#llamo al método perteneciente al objeto
musica_ligera.cantar()
