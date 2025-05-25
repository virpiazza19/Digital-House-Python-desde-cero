# SETS
"""
Es una colección desordenada de elementos únicos. En otras palabras, un conjunto(set) no puede contener elementos duplicados, y no tiene un orden definido. Los conjuntos son útiles cuando necesitas almacenar una colección de elementos sin preocuparte por el orden o la duplicación, y cuando neceistas realizar operaciones matemáticas de conjunto como unión, intersección, diferencia, etc.
"""

# Creación de Sets:

mi_conjunto = {1, 2, 3, 4, 5}

# También es posible crear conjuntos a partir de listas o cualquier otra secuencia utilizando la función set()

lista = [1, 2, 3, 3, 4, 4, 5]

conjunto_desde_lista = set(lista)  # Elimina duplicados

for i in conjunto_desde_lista:
    print(i)
