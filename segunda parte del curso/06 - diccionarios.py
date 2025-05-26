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
diccionario = (
    {
        "nombre": "Virginia",
        "edad": 28,
        "ciudad": "Buenos Aires",
        "profesion": "Software developer",
        "tecnologias": ["Python", "JavaScript"],
    }
)
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
'''-------------------'''
# -------------------------------

# CAMBIAR, AGREGAR Y ELIMINAR PARES CLAVE-VALOR