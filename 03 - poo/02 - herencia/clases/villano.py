from clases.personaje import Personaje


class Villano(Personaje):
    def __init__(self, nombre, salud, habilidad):
        super().__init__(
            nombre, salud
        )  # Constructor de la clase padre (super-clase), es lo que heredo
        self.habilidad = habilidad  # Atributo nuevo, específico de la clase hijo

    def mostrar_habilidad(self):
        print(f"{self.nombre} tiene la habilidad de {self.habilidad}.")
