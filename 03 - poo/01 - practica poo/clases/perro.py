# Definiendo clase (plantilla)

class Perro:
    # Método constructor (__init__)
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Al atributo nombre de la instancia le asignamos el 'nombre' que nos envían como argumento en el constructor
        self.edad = edad  # Al atributo edad de la instancia le asignamos la 'edad' que nos envían como argumento en el constructor

    def ladrar(self):
        return "¡guau!"


"""-----------------------------------------------"""