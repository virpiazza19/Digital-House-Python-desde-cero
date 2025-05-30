class Mago:
    # Método Especial: CONSTRUCTOR
    def __init__(self, nombre, hechizos=None):
        self.nombre = nombre
        self.hechizos = (
            hechizos if hechizos else []
        )  # Cuando se llame al constructor de la clase, este atributo es opcional. En caso de que tenga 'hechizos' se van a popular, caso contratrio crea el atributo como una lista vacía

    # Método Especial: TO STRING (identifico al objeto con una cadena de caractéres)
    def __str__(self):
        return f"¡Hola, mi nombre es {self.nombre}, el mago!"

    # Método Especial: LEN
    def __len__(self):
        return len(self.hechizos)

    # Método Especial: EQ
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.hechizos == otro.hechizos

    # Método Especial: ADD
    def __add__(self,otro):
        if isinstance(otro,Mago):
            return Mago(f"{self.nombre}-{otro.nombre}")
        else:
            raise TypeError("Solo puedes combinar dos magos")