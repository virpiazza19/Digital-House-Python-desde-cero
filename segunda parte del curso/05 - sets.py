# SETS
"""
Es una colección desordenada de elementos únicos. En otras palabras, un conjunto(set) no puede contener elementos duplicados, y no tiene un orden definido. Los conjuntos son útiles cuando necesitas almacenar una colección de elementos sin preocuparte por el orden o la duplicación, y cuando neceistas realizar operaciones matemáticas de conjunto como unión, intersección, diferencia, etc.
"""

# # Creación de Sets:
#
# mi_conjunto = {1, 2, 3, 4, 5}
#
# # También es posible crear conjuntos a partir de listas o cualquier otra secuencia utilizando la función set()
#
# lista = [1, 2, 3, 3, 4, 4, 5]
#
# conjunto_desde_lista = set(lista)  # Elimina duplicados
#
# for i in conjunto_desde_lista:
#     print(i)

# -------------------------------
"""-------------------"""
# -------------------------------

# conjunto_frutas = {
#     "Manzana",
#     "Plátano",
#     "Pera",
#     "Manzana",
# }  # si agrego un elemento repetido no va a aparecer al imprimir
#
# conjunto_frutas = set(("Manzana","Plátano","Pera")) # otra forma de declarar un set/conjunto
#
# conjunto_frutas = set(("Manzana")) # si solo declaro un elemento pasa lo mismo que con las tuplas, va a desagregar los caracteres del elemento en distintos elementos dentro del conjunto, pero en este caso si hay caracteres duplicados no los va a agregar.
#
# conjunto_frutas = set(("Manzana",)) # tal como con las tuplas, si se le agrega la coma ahí agrega al elemento sin desagregar
#
# print(conjunto_frutas)  # el orden en el que se muestran los elementos es aleatorio
#
# # El booleano True con el número 1 -> si ambos elementos están presentes en un set los toma como duplicados
# # El booleano False con el número 0 -> si ambos elementos están presentes en un set los toma como duplicados
#
# conjunto_booleanos = {False, True, 1, 0}
#
# print(conjunto_booleanos) # Devuelve {False, True} o {True, False}
#
# print(len(conjunto_booleanos)) # Devuelve 2
# # al estar duplicados los elementos solo suma la primera instancia del elemento

# -------------------------------
"""-------------------"""
# -------------------------------

# ACCEDER, AGREGAR, Y ELIMINAR ITEMS EN SETS

# conjunto_frutas = {
#     "Frambuesa",
#     "Limón",
#     "Melón",
#     "Lima",
# }

# print(conjunto_frutas[1]) # TypeError: 'set' object is not subscriptable
"""
Al no tener un orden determinado, no se pueden indexar los elementos adentro del set.    
"""
# for fruta in conjunto_frutas:
#     print(fruta)
#
# print("Banana" in conjunto_frutas) # Imprime un booleano - False
# print("Lima" in conjunto_frutas) # Imprime un booleano - True

# AGREGAR ITEMS

# conjunto_frutas = {
#     "Frambuesa",
#     "Limón",
#     "Melón",
#     "Lima",
# }
# conjunto_frutas.add("Arándano")
#
# conjunto_tropicales = {
#     "Mango",
#     "Piña",
#     "Papaya",
#     "Arándano",  # el duplicado no lo agrega
# }
#
# conjunto_frutas.update(conjunto_tropicales)  # se puede agregar un set a otro set
#
# print(conjunto_frutas)
#
# lista_frutas = ["Kiwi", "Naranja"]
#
# conjunto_frutas.update(lista_frutas) # se puede agregar una lista a un set
#
# print(conjunto_frutas)
#
# conjunto_frutas.remove("Naranja") # se puede eliminar un elemento del set
# conjunto_frutas.discard("Papaya") # se puede descartar un elemento del set. Funciona como el remove
#
# conjunto_frutas.pop() # al no estar indexado el set, el elemento que se elimina con pop es aleatorio
#
# conjunto_frutas.clear() # devuelve None
#
# # del conjunto_frutas # al tratar de imprimir el set va a tirar error de código, ya que deja de existir el mismo
#
# print(conjunto_frutas)

# -------------------------------
"""-------------------"""
# -------------------------------

# JUNTAR EN SETS

# conjunto_letras = {"a", "b", "c"}
# conjunto_numeros = {1, 2, 3}
#
# # union = conjunto_letras.union(conjunto_numeros)
# union = conjunto_letras | conjunto_numeros
#
# print(union)

# conjunto_letras = {"a", "b", "c"}
# tupla_numeros = (1, 2, 3)
#
# # union = conjunto_letras | tupla_numeros # en este caso no se puede unir un set y una tupla
# union = conjunto_letras.union(tupla_numeros) # devuelve un set que se lo asigna a una variable de tipo set
#
# conjunto_letras.update(tupla_numeros) # en este caso no devuelve set, ya que está actualizando el mismo conjunto
#
# print(union)
# print(conjunto_letras)

## set_chicago = {"Python", "JavaScript", "AWS"}
## set_oxford = {"Python", "TypeScript", "GoogleCloud"}
##
## set3 = set_chicago.intersection(set_oxford)  # valores en comun
## set3 = set_chicago & set_oxford  # valores en comun
##
## print(set3)
##
## # set_chicago.intersection_update(set_oxford)  # actualiza el conjunto dejando solo aquellos valores que se repiten en ambos conjuntos
## # print(set_chicago)
##
## set4 = set_chicago.difference(set_oxford) # valores diferentes de set_chicago
## print(set4)
##
## set5 = set_oxford.difference(set_chicago) # valores diferentes de set_oxford
## print(set5)
##
## set6 = set_chicago - set_oxford # elimina del primer set los elementos que se encuentran en el segundo
## print(set6)

# BUCLES EN SETS

conjunto_frutas = {"Frambuesa","Limón","Melón","Lima"}

for fruta in conjunto_frutas:
    print(fruta)

""" Al no tener índices, no se pueden utilizar WHILE, RANGE """
