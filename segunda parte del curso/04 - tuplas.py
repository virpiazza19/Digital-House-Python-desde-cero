# TUPLAS
"""
Una tupla en Python es una estructura de datos similar a una lista, pero con la principal diferencia de que es inmutabla, es decir, una vez creada, no se puede modificar.
Las tuplas se utilizan para almacenar colecciones ordenadas de elementos de diferentes tipos, al igual que las listas.
"""

# Creación de Tuplas:

# mi_tupla = (1, 2, 3, 4, 5)

# También se pueden crear tuplas sin paréntesis, simplemente separando los elementos por comas.
# Sin embargo, se recomienda el uso de paréntesis para mayor claridad y consistencia

# otra_tupla = 10, 20, 30

# -------------------------------
"""-------------------"""
# -------------------------------

# frutas1 = ("Manzana", "Plátano", "Cereza", "Manzana")

# print(frutas1) # Devuelve la tupla -('Manzana', 'Plátano', 'Cereza', 'Manzana')- acepta duplicados como cualquier lista

# frutas2 = ("Manzana", "Plátano", "Cereza", "Manzana")

# print(len(frutas2)) # Devuelve 4

"""
Para que una tupla exista como tal debe tener al menos un elemento. Pero para que se entienda que es una tupla debemos agregar una coma luego de ese único elemento, ya que sino lo interpreta como un str.

frutas3 = ("Manzana", "Plátano", "Cereza", "Manzana")

print(type(frutas3)) # Devuelve <class 'tuple'>

frutas4 = ("Manzana")

print(type(frutas4)) # Devuelve <class 'str'>

frutas5 = ("Manzana",)

print(type(frutas5)) # Devuelve <class 'tuple'>
"""

# frutas = tuple(("Manzana", "Plátano", "Mandarina"))
# print(frutas)

"""
frutas = tuple(("Manzana")) # En este caso si se crea con solo un elemento, al crearse la tupla va a separar el elemento y va a crear un elemento en 'frutas' por cada caracter del mismo
print(frutas)

frutas = tuple(("Manzana",)) # Al agregar la coma al final lo agrega como un único elemento
print(frutas)
"""

# -------------------------------
"""-------------------"""
# -------------------------------

# ITEMS EN TUPLAS

# índices    #0       #1      #2         #3           #4         #5        #6
# frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")

# Se puede acceder a cada ítem de la misma forma que con las listas

"""
print(frutas[2:])

if "Kiwi" in frutas:
    print("Si, hay Kiwi")
"""

# -------------------------------
"""-------------------"""
# -------------------------------

# ACTUALIZACIÓN DE TUPLAS
# (cómo saltear la restricción de inmutabilidad si hiciese falta)

# frutas[1] = "Coco" # TypeError: 'tuple' object does not support item assignment

# print(frutas)

# frutass = list(frutas) # creo una copia de la tupla en formato lista

# frutass[2] = "Coco" # modifico la lista

# frutas = tuple(frutass) # convierto a tupla la lista y la reasigno a la tupla original

"""
Si bien es inmutable, se pueden usar los casteos de list() y tuple() para momentáneamente 'convertir' una tupla en lista, modificarla y luego volverla al tipo original.
No es recomendado usarlas todo el tiempo, solo cuando sea realmente necesario.
Si se tiene que modificar varias veces es mejor usar una lista
"""

# frutasss = list(frutas)  # creo una copia de la tupla en formato lista
#
# frutasss.append("Coco")  # agrego un valor a la lista
#
# frutas = tuple(frutasss)  # convierto a tupla la lista y la reasigno a la tupla original
#
# print(frutas)

# tupla_verduleria = (
#    "Manzana",
#    "Uva",
#    "Fresa",
#    "Mandarina",
#    "Aguacate",
#    "Naranja",
#    "Kiwi",
# )
# tupla_vegetales = (
#    "Lechuga",
#    "Papa",
#    "Batata",
#    "Calabaza",
#    "Morron",
#    "Cebolla",
#    "Brocoli",
# )

# Forma clásica de fusionar las tuplas
# lista_frutas_y_verduras = list(tupla_verduleria) + list(tupla_vegetales)
# tupla_verduleria = tuple(lista_frutas_y_verduras)
# print(tupla_verduleria)}

# Forma más simple y optimizada, forma más fácil de agrgar items a la tupla evitando escribir líneas de código para castear a list() y recastear a tuple()

# tupla_verduleria += tupla_vegetales

# print(tupla_verduleria)
#
## Eliminar items de una tupla
#
# lista_verduleria = list(tupla_verduleria)
# lista_verduleria.remove("Uva")
# tupla_verduleria = tuple(lista_verduleria)
#
# print(tupla_verduleria)

## Eliminar tupla
#
# del tupla_vegetales
#
# print(tupla_vegetales) #Undefined name `tupla_vegetales`RuffF821 - error porque eliminamos la tupla en la línea anterior

# -------------------------------
"""-------------------"""
# -------------------------------

# DESEMPAQUETADO DE TUPLAS
# (asignar a distintas variables, distintos elementos de una tupla)

"""NO se puede desempaquetar una tupla por partes"""

# tupla_fruta = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")

"""
(a, b, c, d, e, f, g) = tupla_fruta # asignar valores de una tupla a distintas variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
"""

"""
(a, b, c, *d) = tupla_fruta 
print(a) # devuelve Manzana
print(b) # devuelve Uva
print(c) # devuelve Fresa
print(d) # devuelve ['Mandarina', 'Aguacate', 'Naranja', 'Kiwi']}
"""

"""
(a,*b,c) = tupla_fruta
print(a) # devuelve Manzana
print(b) # devuelve ['Uva', 'Fresa', 'Mandarina', 'Aguacate', 'Naranja']
print(c) # devuelve Kiwi
"""

# -------------------------------
"""-------------------"""
# -------------------------------

# BUCLES EN TUPLAS

"""
tupla_frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Naranja", "Kiwi")
"""

# for fruta in tupla_frutas:
#     print(fruta)

# for i in range(len(tupla_frutas)):
#    print(tupla_frutas[i], "con el índice",i)

# i = 0
# while i < len(tupla_frutas):
#     print(tupla_frutas[i], "con el índice",i)
#     i +=1

# -------------------------------
"""-------------------"""
# -------------------------------

# UNIÓN EN TUPLAS
# (juntar, contar y ver índice de ítems)

# tupla_frutas_1 = ("Manzana", "Uva", "Fresa")
# tupla_frutas_2 = ("Mandarina", "Naranja", "Kiwi", "Manzana")
# 
# # tupla_frutas = tupla_frutas_1 + tupla_frutas_2
# 
# tupla_frutas = tupla_frutas_1 * 5 + tupla_frutas_2  # Se puede multiplicar el tamaño
# 
# print(tupla_frutas)
# print(tupla_frutas.count("Manzana"))
