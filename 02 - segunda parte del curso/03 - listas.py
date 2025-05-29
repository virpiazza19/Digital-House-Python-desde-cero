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

"""frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Ananá"]"""

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

# COMPRENSIÓN DE LISTAS: ABREVIACIONES

"""frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Fresa", "Ananá"]"""
# Modo tradicional
"""
frutas_con_e = []

for fruta in frutas:
    if "e" in fruta:
        frutas_con_e.append(fruta)
print(frutas_con_e)
"""

# Modo abreviado

# lista        # dato      # bucle         # condición
"""frutas_con_e = [fruta for fruta in frutas if "e" in fruta]"""

# print(frutas_con_e)

# lista      # dato      # condición con else              # bucle
"""frutas_dos = [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas]"""

# print(frutas_dos)

# -------------------------------
# -------------------------------

# ORDENAMIENTO DE LISTAS

"""
frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Fresa", "Ananá"]
frutas.sort()  # ordena en forma ascendente
print(frutas)
"""

"""
numeros = [9, 999, 88, 1, 2, 3, 4, 5, 2, 33, 4]
# numeros.sort()  # ordena en forma ascendente
numeros.sort(reverse=True) # ordena en forma ascendente
print(numeros)
"""
"""
frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Fresa","pera", "Ananá","manzana"]
frutas.sort()  # ordena en forma ascendente pero no toma ordena correctamente los elementos que comienzan en minúscula. Es case sensitive
frutas.sort(key = str.lower) # ordena teniendo sin tener en cuenta si la primera letra es mayúscula o minúscula
frutas.reverse() # ordena a la inversa el orden original, utiliza los índices del 7 al 0
print(frutas)
"""

# -------------------------------
# -------------------------------

# COPIAR Y JUNTAR LISTAS

'''
# COPIAR
frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Fresa", "Ananá"]

# -------------------
copia_frutas = frutas.copy()

print(copia_frutas)
# -------------------
copia_frutas_dos = list(frutas)

print(copia_frutas_dos)
# -------------------
copia_frutas_tres = [fruta for fruta in frutas]

print(copia_frutas_tres)
# -------------------

'''
# JUNTAR
frutas_uno = ["Manzana", "Banana", "Pera"]
frutas_dos = ["Mandarina", "Fresa", "Ananá"]

'''
frutas = frutas_uno + frutas_dos
print(frutas)

frutas_uno.extend(frutas_dos)
print(frutas_uno)
'''
# NO se recomienda porque puede realentizar la performance, además de que son demasiadas líneas de código
'''
frutas_tres = []

for fruta in frutas_uno:
    frutas_tres.append(fruta)
for fruta in frutas_dos:
    frutas_tres.append(fruta)
print(frutas_tres)'''