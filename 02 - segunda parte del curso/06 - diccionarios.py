# DICCIONARIOS
"""
Un diccionario en Python es una estructura de datos que permite almacenar pares de datos llamados "clave/valor". Cada elemento en un diccionario consta de una clave única y su correspondiente valor. Las claves suelen ser de tipo inmutable (como strings o números), mientras que los valores pueden ser de cualquier tipo (números, strings, listas, diccionarios, etc.).
"""

# Creación de Diccionarios:

## mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Para acceder a un valor en un diccionario se utiliza la clave correspondiente

## print(mi_diccionario["nombre"])  # Imprime "Juan"
## print(mi_diccionario["edad"])  # Imprime 30

# -------------------------------
"""-------------------"""
# -------------------------------

# NO TIENEN ÍNDICE y no mantienen un orden los elementos, pero si hay un orden en las propiedades (clave/valor) dentro de cada ítem
"""
diccionario = {
    "nombre": "Virginia",
    "edad": 28,
    "ciudad": "Buenos Aires",
    "profesion": "Software developer",
    "tecnologias": ["Python", "JavaScript"],
}
"""
# print(diccionario)
# print(diccionario["nombre"]) # imprime cuando hay un solo elemento
# print(diccionario["tecnologias"]) # imprime cuando hay un solo elemento

# nombre = diccionario.get("nombre")
# print(nombre)  # Virginia
#
# claves = diccionario.keys()
# print(claves)  # dict_keys(['nombre', 'edad', 'ciudad', 'profesion', 'tecnologias'])
#
# diccionario["nombre_completo"] = (
#     "Virginia Maria Piazza"  # Se puede utilizar para actualizar un valor en una clave existente, o mismo se puede usar para crear una nueva clave
# )
#
# print(diccionario)
#
# valores = diccionario.values()
#
# print(valores)

## items = diccionario.items() # lista de tuplas, lista donde cada elemento es una tupla compuesta por clave y valor
##
## print(items)

### if "nombre" in diccionario:
###     print("Existe la clave nombre")
###
### if "apellido" in diccionario:
###     print("Existe la clave apellido")
### else:
###     print("No existe apellido")

# -------------------------------
"""-------------------"""
# -------------------------------

# CAMBIAR, AGREGAR Y ELIMINAR PARES CLAVE-VALOR

# diccionario["nombre"] = "Virginia Maria Piazza"  # actualizamos el valor existente
# diccionario.update(
#     {"nombre": "Virginia Piazza", "edad": 27}
# )  # actualizamos uno o más valores
#
# diccionario["pais"] = "Argentina"  # agregamos una propiedad
# diccionario.update({"fecha_nacimiento": "19/06/1997"})  # agregamos una propiedad
#
# # print(diccionario)
#
# diccionario.pop(
#     "pais"
# )  # eliminamos el par clave-valor que le pasamos como parámetro - en este caso pais
# diccionario.popitem()  # se elimina el último par - en este caso fecha_nacimiento
# # diccionario.popitem() # se elimina el último par existente
# # diccionario.popitem() # se elimina el último par existente
# # diccionario.popitem() # se elimina el último par existente
# # diccionario.popitem() # se elimina el último par existente
# # diccionario.popitem() # se elimina el último par existente
# # Si con el popitem eliminamos todos los pares clave-valor nos devuelve {}
# print(diccionario)
#
# del diccionario["nombre"]  # eliminamos una propiedad específica
# ## del diccionario # eliminamos el diccionario entero por lo que daría error si intentamos llamarlo en algún método o función
#
# print(diccionario)
#
# diccionario.clear()  # vacía el diccionario pero no lo elimina
#
# print(diccionario)

# -------------------------------
"""-------------------"""
# -------------------------------

# COPIAR DICCIONARIOS Y UTILIZACIÓN DE BUCLES

"""
diccionario = {
    "nombre": "Virginia",
    "edad": 28,
    "ciudad": "Buenos Aires",
    "profesion": "Software developer",
    "tecnologias": ["Python", "JavaScript"],
}

## diccionario2 = diccionario  # de esta forma no se estaría copiando el diccionario, sino que creo una variable de tipo diccionario que hace referencia al diccionario original -NO USAR

diccionario2 = diccionario.copy() # copiamos toda la información dentro del diccionario en uno nuevo
diccionario2 = dict(diccionario) # copiamos el diccionario usando el constructor

## diccionario["edad"] = 27 # cuando usamos diccionario2 = diccionario y modificamos diccionario, automáticamente el valor de edad refiere al actualizado

# print(diccionario2)

for key in diccionario: # itera sobre la clave
    print(key) # imprimo las claves
    print(diccionario[key]) # imprimo los valores
    print("Clave:",key,"| Valor:",diccionario[key])
    
for value in diccionario.values(): # itero sobre los valores
    print(value)

# Desestructuración / Desempaquetamiento
for x,y in diccionario.items(): # itero sobre los items en general
    print(x,y)
    print(x)
    print(y)
"""

# -------------------------------
"""-------------------"""
# -------------------------------

# DICCIONARIOS ANIDADOS

familia = {
    "padre": {"nombre": "Raul", "profesion": "Carpintero"},
    "madre": {"nombre": "Patricia", "profesion": "Abogada"},
    "hijo": {"nombre": "Pedro", "profesion": "desempleado"},
}

"""
padre = ({"nombre": "Raul", "profesion": "Carpintero"},)
madre = ({"nombre": "Patricia", "profesion": "Abogada"},)
hijo = {"nombre": "Pedro", "profesion": "desempleado"}
"""

# print(familia["padre"]["profesion"])

for (
    pariente,
    data,
) in familia.items():  # iteramos sobre los items dentro del diccionario general
    print(pariente)  # imprimimos la clave dentro del diccionario general
    for clave in data:  # iteramos sobre las claves dentro del diccionario anidado
        print(
            clave + ":", data[clave]
        )  # imprimimos la clave y su respectivo valor dentro del diccionario anidado
