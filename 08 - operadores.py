# OPERADORES

# Símbolos o conjuntos de símbolos que realizan una operación específica en uno o más operandos

# TIPOS: Aritméticos - Asignación - Comparación - Lógicos -  Indentidad - Pertenencia

# -------------------------------

# OPERADORES ATIRMÉTICOS

# + para sumar
# - para restar
# * para multiplicar
# / para dividir
# // para dividir entero (floor division)
# % resto o módulo (modulus)
# ** exponenciación

a = 6
b = 4

c = a + b  # suma
# print(c)
d = a - b  # resta
# print(d)
e = a * b  # multiplicación
# print(e)
f = a / b  # división
# print(f)
g = a // b  # división exacta (redondea)
# print(g)
h = a % b  # devuelve el resto
# print(h)
i = a**b  # exponencia
# print(i)

# -------------------------------

# OPERADORES DE ASIGNACIÓN

# '=' asignación general
# '+='
# '-='
# '*='
# '/='
# '//='
# '='

x = 10
sumatorio = 3

# 10
x += sumatorio  # 13
x += sumatorio  # 16
x += sumatorio  # 19
x += sumatorio  # 22

# print(x)

# ------------------

x = 10
aRestar = 2

# 10
x -= aRestar  # 8
x -= aRestar  # 6
x -= aRestar  # 4
x -= aRestar  # 2

# print(x)

# ------------------

x = 10
factor = 2

# 10
x *= factor  # 20
x *= factor  # 40
x *= factor  # 80
x *= factor  # 160

# print(x)

# ------------------

x = 20
divisor = 2

# 10
x /= divisor  # 10
x /= divisor  # 5
x /= divisor  # 2.5
x /= divisor  # 1.25

# print(x)

# ------------------

x = 20
divisor = 2

# 10
x //= divisor  # 10
x //= divisor  # 5
x //= divisor  # 2
x //= divisor  # 1

# print(x)

# -------------------------------

# OPERADORES DE COMPARACIÓN

# No es lo mismo que el = para asignar que dos = (==)

# == igualdad
# != diferencia
# ! o not negación
# < menor
# > mayor
# <= menor o igual
# >= mayor o igual

x = 5
y = 4

# print(x == y)  # booleano
# print(x != y)  # booleano
# print(x < y)
# print(x > y)
# print(x <= y)
# print(x >= y)

# -------------------------------

# OPERADORES LÓGICOS

# and -> true si y solo si ambas afirmaciones son verdaderas
# or -> true si alguna de las afirmaciones es verdadera
# not -> devuelve el opuesto al valor de la afirmación

x = 5

booleano = x > 3 and x < 10

# print(booleano) # True

x = 15

booleano = x > 3 and x < 10

# print(booleano) # False

x = 15

booleano = x > 3 or x < 10

# print(booleano) # True

x = 0

booleano = x >= 0 or x != 10

# print(booleano) # True

x = 0

booleano = x > 0 or x != 0

# print(booleano) # False

x = 0

booleano = x > 0 and x != 0

# print(booleano) # False

x = 50

booleano = not x == 0

# print(booleano) # True

# -------------------------------

# OPERADORES DE IDENTIDAD

# 'is'
# 'is not'

a = 5
b = 5

booleano = a is b

# print(booleano)

a = "Esto es un texto"
b = "Esto es un texto "

booleano = a is b

# print(booleano)

a = "Esto es un texto"
b = "Esto es un texto "

booleano = a is not b

# print(booleano)

# -------------------------------

# OPERADORES DE PERTENENCIA

# 'in'
# 'not in'

texto = "En este texto pondremos algunas tecnologías: Python, R, Django, TensorFlow"

# print("Django" in texto)
# print(("Django").lower() in texto.lower())
# print("JavaScript" not in texto)

# -------------------------------
