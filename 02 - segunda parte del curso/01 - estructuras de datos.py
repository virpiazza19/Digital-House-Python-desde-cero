# ESTRUCTURAS DE DATOS

# En Python, una estructura de datos es una forma de organizar y almacenar datos de manera que puedan ser utilizados eficientemente. Estas estructuras proporcionan métodos para insertar, acceder, modificar, y eliminar datos de manera ordenada y eficiente.

# Las estructuras de datos en Python pueden ser simples, como listas y tuplas, o más complejas, como diccinarios y conjuntos. Cada tipo de estructura de datos tiene sus propias características y métodos que facilitan diversas operaciones.

# -------------------
# SECUENCIA / COLECCIÓN
# -------------------

# - list (lista) [colección ordenada y mutante]
lista = [1, 2, 3, 4]

# - tuple (tupla) [colección ordenada e inmutable]
tupla = (1, 2, 3)

# - range (rango) [secuencia inmutanlr de números]
rango = range(0, 10)

# -------------------
# MAPPING TYPE (mapeo)
# -------------------

# - dict (diccionario)[colección no ordenada de pares clave-valor]
diccionario = {
    "nombre": "Sergie",  # más fácil para leer y más ordenado
    "edad": 24,
}

# -------------------
# SET TYPE (conjunto)
# -------------------

# - set (conjunto) [colección no ordenada y mutable de elementos únicos (no permite repetir)]
conjunto = {1, 2, 3, 4}

# - frozenset (conjunto inmutable) [conjunto inmutable de las mismas características que el set]
conjunto_inmutable = frozenset({1, 2, 3, 4})

#-------------------
# NONE/NULL TYPES (nulos)
#-------------------

# - noneType [ausencia de valor o la no definición]
nulo = None