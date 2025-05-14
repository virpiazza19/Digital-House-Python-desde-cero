
# TIPOS DE DATOS

# -------------------
# TEXTO
# -------------------

# - str -> string -> cadena de caracteres -> secuencia de caracteres unicode
texto = "Cadena de caracteres"

# -------------------
# NUMERICOS
# -------------------

# - int (entero)
numero_entero = 10

# - float (flotante)
numero_flotante = 3.14

# - complex (complejo)
numero_complejo = 2 + 3j

# -------------------
# SECUENCIA
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
# BOOLEANO TYPES (booleano)
#-------------------

# - boolean [puede ser verdadero o falso]
booleano = True
booleano2 = False

#-------------------
# BINARY TYPES (binarios)
#-------------------

# - bytes [secuencia inmutable de bytes]
bytes_data = b"datos"

# - bytearray (array de bytes) [secuencia mutable de bytes]
bytearray_data = bytearray(b"datos")

# - memoryview (vista de memoria) [permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b"datos")

#-------------------
# NONE/NULL TYPES (nulos)
#-------------------

# - noneType [ausencia de valor o la no definición]
nulo = None