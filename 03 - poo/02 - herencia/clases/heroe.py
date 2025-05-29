from clases.personaje import Personaje


class Heroe(Personaje):
    def __init__(self, nombre, salud, poder):
        super().__init__(
            nombre, salud
        )  # Constructor de la clase padre (super-clase), es lo que heredo
        self.poder = poder  # Atributo nuevo, específico de la clase hijo

    def mostrar_poder(self):
        print(f"{self.nombre} tiene el poder de {self.poder}.")
