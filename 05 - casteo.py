
# CASTEO (cambio de tipo de dato)

# tipoDeDato(datoOriginal)
# con type(datoOriginal) -> qué tipo de dato estoy usando

# Texto (str)
variable1 = "Texto"
variable2 = "123456"
variable3 = "Texto123"

# Numéricas (int, float, complex)
variable4 = 10
variable5 = 2.5
variable6 = 1j

print(type(variable1))  # <class 'str'>
print(type(variable2))  # <class 'str'>
print(type(variable3))  # <class 'str'>
print(type(variable4))  # <class 'int'>
print(type(variable5))  # <class 'float'>
print(type(variable6))  # <class 'complex'>

# casteo de str a int
print(type(variable2))  # <class 'str'>
print(int(variable2))  # <class 'int'>
print(type(int(variable2)))  # <class 'int'>

# -------------------------------

lista = ["manzana", "pera", "naranja"]

x = list(("manzana", "pera", "naranja"))

print(type(lista))
print(type(x))

#-------------------------------

tupla = ("manzana", "pera", "naranja")
list = list(tupla)

print(type(list))

