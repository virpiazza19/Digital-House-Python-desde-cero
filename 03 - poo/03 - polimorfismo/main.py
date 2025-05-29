from clases.perro import Perro
from clases.gato import Gato
from clases.vaca import Vaca

# POLIMOFFISMO: capacidad de los objetos de diferentes clases de responder al mismo método de forma distinta


def hacer_sonido_de_animal(animal):
    print(f"{animal.nombre} hace {animal.hacer_sonido()}")


perro = Perro("Max")
gato = Gato("Garfield")
vaca = Vaca("Lola")

hacer_sonido_de_animal(perro)  # Devuelve: Guau guau
hacer_sonido_de_animal(gato)  # Devuelve: Miau miau
hacer_sonido_de_animal(vaca)  # Devuelve: Muuuuuu
