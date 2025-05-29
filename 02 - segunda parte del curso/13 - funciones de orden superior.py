# FUNCIONES DE ORDEN SUPERIOR
# (map, filter y reduce. Uso de lambda y callbacks)

from functools import reduce  # línea 48

"""Funciones que reciben y devuelven funciones como argumentos"""

# -------------------------------
"""-------------------"""
# -------------------------------

# MAP
""" Toma una función y un iterable (ej, lista) como argumentos y aplica la función a cada elemento del iterable."""


def cuadrado_map(x):
    return x * x


numeros_map = [1, 2, 3, 4, 5]

cuadrados_map = list(map(cuadrado_map, numeros_map))

# print(cuadrados_map)

# -------------------------------
"""-------------------"""
# -------------------------------

# FILTER
""" Toma una función que devuelve True o False y un iterable, y devuelve solo los elementos que devuelvan True como argumento de la función."""


def esPar_filter(x):
    return x % 2 == 0


numeros_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

pares_filter = list(filter(esPar_filter, numeros_filter))

# print(pares_filter)

# -------------------------------
"""-------------------"""
# -------------------------------

# REDUCE
""" Toma una función binaria (dos parámetros/argumentos) y un iterable, y aplica la función de forma acumulativa a los elementos del iterable."""


def suma_reduce(x, y):
    return x + y


numeros_reduce = [1, 2, 3, 4, 5]

sumatoria_reduce = reduce(suma_reduce, numeros_reduce)

# print(sumatoria)

# -------------------------------
"""-------------------"""
# -------------------------------

# LAMBDA

numeros_lambda = [1, 2, 3, 4, 5]

cuadrados_lambda = list(map(lambda x: x * x, numeros_lambda))

# print(cuadrados_lambda)

"""-------------------"""

numeros_lambda2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

pares_lambda = list(filter(lambda x: x % 2 == 0, numeros_lambda2))

# print(pares_lambda)
