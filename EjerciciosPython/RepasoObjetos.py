# clase extra POO
# definir clase auto
class Auto:
    # crear el método constructor
    def __init__(self, marca, modelo, anio,
                 tipo):  # parámetro self: es un parámetro implicito que indica que se trata del objeto actual
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = tipo

    def en_marcha(self, arrancando):
        if arrancando:
            print("El auto está en marcha")
        else:
            print("El auto está apagado")

    def __str__(self):
        print(f"El auto de marca {self.marca}, modelo  {self.modelo} es del año {self.anio} y es {self.tipo}")


# instanciar la clase: crear un objeto  perteneciente a dicha clase

class Descapotable(Auto):  # La clase Descapotable es subclase de la clase Auto, lo indico pasándoselo como parámetro
    # Defino método constructor
    def __init__(self, marca, modelo, anio, tipo, techo):
        super().__init__(marca, modelo, anio, tipo)
        self.techo = techo

    def estado(self):
        if self.techo:
            print("El auto es descapotable totalmente")
        else:
            print("El auto tiene una ventana en el techo")

    def __str__(self):
        print(f"El auto es un {self.marca} {self.modelo} {self.tipo} de {self.anio}, y es descapotable")


cupe = Descapotable("Renault", "Coupeé", 1980, "full", True)
cupe.__str__()
cupe.estado()
