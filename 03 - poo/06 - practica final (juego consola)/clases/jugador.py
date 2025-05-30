import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        # Como son valores por defecto, no es necesario pasarlos como argumentos en el constructor
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0

    def atacar(self):
        return random.randint(10, 20) * self.nivel

    def recibir_danio(self,danio):
        self.salud -= danio
        if self.salud <= 0:
            print(f"{self.nombre} ha muerto. ¡Game Over!")
        else:
            print(f"Te quedan {self.salud} puntos de salud")
        
    def ganar_experiencia(self,experiencia):
        self.experiencia += experiencia
        print(f"{self.nombre} ha ganado {experiencia} puntos de experiencia.")
        if self.experiencia >= 100:
            self.nivel +=1
            self.experiencia = 0
            print(f"{self.nombre} ha subido al nivel {self.nivel}")