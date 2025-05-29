# Importo la clase Perro del archivo perro.py
from clases.perro import Perro

"""-----------------------------------------------"""

# Creo instancias de la clase Perro

# 'perro1' es un objeto de la clase Perro
perro1 = Perro("Max", 11)  # Llamo al constructor pasando como argumentos nombre y edad
# 'perro2' es un objeto de la clase Perro
perro2 = Perro("Pepo", 9)  # Llamo al constructor pasando como argumentos nombre y edad

"""-----------------------------------------------"""

# Uso template strings (f"{}") con las variables propias de la 'instancia de una clase' (objeto)
print(f"{perro1.nombre} tiene {perro1.edad} años y dice {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice {perro2.ladrar()}")
