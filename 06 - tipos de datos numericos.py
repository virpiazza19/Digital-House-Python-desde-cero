# TIPOS DE DATOS NUMERICOS

# x = 1 #int
# x1 = -1 #int
# x2 = 0 #int

# y = 2.8 #float
# y1 = -2.8 #float
# y2 = 0.0 #float

# z = 2j #complex
# z1 = -2j #complex
# z2 = 5+2j #complex
# z3 = 0 #complex

# -------------------------------

# a = 5
# b = float(a)

# print(b)
# print(type(b))

# -------------------------------

# c = 5.5
# d = int(c)

# print(d)
# print(type(d))

# -------------------------------

# e = 5j
# f = int(e) #No se puede cambiar el tipo de un número complejo

# print(f)
# print(type(f))

# -------------------------------

# RANGOS DE ALEATORIDAD

import random

g = random.randrange(1, 10)  # no incluye el 10

print(g)

h = random.random() # devuelve flotante

print(h)
print(type(h))

i = random.randint(1, 10) # incluye el 10

print(i)
print(type(i))
