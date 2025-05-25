# LISTAS
"""
Una lista en Python es una estructura de datos que permite almacenar una colección ordenada de elementos. Estos elementos pueden ser de cualquier tipo (números, strings, booleanos, incluso otras listas) y pueden ser modificados una vez que la lista ha sido creada.
"""

# Creación de Listas:

# mi_lista = [1, 2, 3, 4, 5]

# También es posible crear listas vacías, y luego agregar elementos a ellas:

"""
lista_vacia = []
lista_vacia.append(10)
lista_vacia.append(20)
lista_vacia.append(30)
lista_vacia.append(40)
"""

# -------------------------------
"""
# índices:
# nombre   0(-6)      1(-5)    2(-4)     3(-3)        4(-2)     5(-1)
lista = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Ananá"]
lista2 = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Ananá"]
tupla = ("Mandarina", "Frutilla", "Ananá")
"""

# print(lista)
# print(lista[0]) # primera posición
# print(lista[-1])  # última posición
# print(lista[2:5]) # el último elemento no está incluído -['Pera', 'Mandarina', 'Frutilla']-

# if "Mandarina" in lista:
#    print("Si, mandarina está en la lista")

"""
lista[1] = "Plátano"
lista[4] = "Fresa"
lista[5] = "Piña"
"""

# lista[4:]=["Fresa","Piña"] # reemplazo los valores desde la posición 4 en adelante
# lista[1:3]=["Plátano","Aguacate"] # reemplazo los valores desde el índice 1 al 3 exclusive

# print(lista[4])
# lista.insert(2,"Palta") # dependiendo de donde insertemos puede que el orden de los índices se vea afectado
# print(lista[4])

# lista.append("Palta") # append va a colocar el valor nuevo en la última posición

# lista.extend(lista_dos) # como un join de sql. fusiono ambas listas
# lista.extend(tupla) # la tupla es inmutable, pero en este caso no la modifico, sino que extraigo los valores para agregarlos a la lista

# print(lista)

# -------------------------------
# -------------------------------

"""
lista = ["Manzana", "Banana", "Pera","Mandarina", "Frutilla", "Ananá"]

# lista.remove("Pera") # elimina el primer valor que encuentra igual
# lista.pop(2) # elimina el valor que se encuentra en el índice declarado

# lista.pop() # cuando no se le pasa el índice elimina el último elemento de la lista

# del lista[3] # elimina el valor que se encuentra en el índice declarado
# del lista # elimina la lista entera, pero en este caso si tengo declarado imprimir cualquier dato que haya en la lista va a tirar error porque al estar vacía, la lista deja de existir

lista.clear() # limpia la lista, dejando un valor none

print(lista)
"""

# -------------------------------
# -------------------------------

# BUCLES EN LISTAS

# FOR

frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Ananá"]

""" bucle for abreviada """
# abreviación del código standard
# [print(fruta) for fruta in frutas] 

""" bucle for 'standard'"""
# for fruta in frutas:
#    print(fruta)

""" bucle for con índice disponible"""
# for i in range(len(frutas)):
#    print(i,frutas[i])
#
# print(len(frutas))

# WHILE
# (tiene disponible el índice)
# i = 0
# while i < len(frutas):
#     print(frutas[i])
#     i += 1

# -------------------------------
# -------------------------------
