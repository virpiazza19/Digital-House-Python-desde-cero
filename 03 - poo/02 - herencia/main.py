from clases.heroe import Heroe
from clases.villano import Villano

superman = Heroe("Superman", 100, "volar")  # Creamos el objeto de Heroe

joker = Villano("Joker", 80, "robar bancos")  # Creamos el objeto de Villano

# -------------------------------

superman.identificarse()  # Método heredado de Personaje
superman.mostrar_salud()  # Método heredado de Personaje

superman.mostrar_poder()  # Método (comportamiento) propio de Heroe

"""--------------------------------------------------------------------"""

joker.identificarse()  # Método heredado de Personaje
joker.mostrar_salud()  # Método heredado de Personaje

joker.mostrar_habilidad()  # Método (comportamiento) propio de Villano
