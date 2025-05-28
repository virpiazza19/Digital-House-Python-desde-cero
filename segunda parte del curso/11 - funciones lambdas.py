# FUNCIONES LAMBDA
# (también conocidas como funciones anónimas, que pueden definirse en una línea de código)

# def duplicar(num):
#     return num*2
#
# # print(duplicar(5))
#
# duplicar_lambda = lambda num: num*2
#
# # print(duplicar_lambda(3))

## def multiplicar(a,b):
##     return a*b
##
## # print(multiplicar(5,10))
##
## multiplicar_lambda = lambda a,b: a*b
##
## # print(multiplicar_lambda(3,4))


### def cuadrado(num):
###     return num * num
###
###
### # print(cuadrado(5))
###
### cuadrado_lambda = lambda num: num * num
###
### # print(cuadrado_lambda(3))

"""-------------------"""

"""-------------------"""

# LAMBDA DENTRO DE OPERACIONES


def operaciones(operacion):
    if operacion == "suma":
        return lambda x, y: x + y
    elif operacion == "resta":
        return lambda x, y: x - y
    elif operacion == "multiplicacion":
        return lambda x, y: x * y
    else:
        return lambda x, y: x / y


suma = operaciones("suma")

# print(suma(2,5))


def multiplicador(n):
    return lambda x: x * n


triplicar = multiplicador(3)

# print(triplicar(5))

"""-------------------"""

estudiantes = [
    {"nombre": "Juan", "edad": 20},
    {"nombre": "Maria", "edad": 25},
    {"nombre": "Pedro", "edad": 22},
]

estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["edad"])

# print(estudiantes_ordenados)
