# def mostrar_mercaderia(mercaderia):
#     for item in mercaderia:
#         print(item)
#
# lista_frutas=["Manzana", "Pera", "Banana"]
#
# mostrar_mercaderia(lista_frutas)

"""-------------------"""

## def suma(a, b):
##     resultado = a + b  # variable local (solo está disponible dentro de la función)
##     return resultado
##
##
## resultado = suma(2, 3)  # variable global
##
## print(resultado)

"""-------------------"""

### def suma(a, b):
###     """Si tengo que declarar la función pero todavía no tengo el código completo puedo agregar pass para que el código en general no se rompa y pueda saltar a la siguiente acción fuera de la declaración de la función"""
###     pass
###
###
### resultado = suma(2, 3)
###
### print(
###     resultado
### )  # en este caso como la función tiene el 'pass' el print va a devolver 'None'

"""-------------------"""


from operator import mul


def devolver_cuadrado(x):
    """Devuelve el cuadrado del valor de x"""
    return x**2


# print(devolver_cuadrado(x=3))  # key word argument -> devuelve: 9

"""
En el caso de que no querramos que se acepten Key Word Arguments, la forma de restringirlo es con ',/'
"""

#### def devolver_cuadrado2(x, /):
####     """Devuelve el cuadrado del valor de x"""
####     return x**2
####
####
#### print(
####     devolver_cuadrado2(x=2)
#### )  # TypeError: devolver_cuadrado2() got some positional-only arguments passed as keyword arguments: 'x'
####
#### print(devolver_cuadrado2(2))  # devuelve: 4

"""
En el caso de que querramos que solo se acepten Key Word Arguments, la forma de especificarlo es con '*,'
"""

##### def devolver_cuadrado3(*, x):
#####     """Devuelve el cuadrado del valor de x"""
#####     return x**2
#####
#####
##### print(devolver_cuadrado3(x=2))  # devuelve: 4

##### print(
#####     devolver_cuadrado3(2)
##### )  # TypeError: devolver_cuadrado2() got some positional-only arguments passed as keyword arguments: 'x'

"""-------------------"""


def calcular_resultado(a, b, /, *, c, d):
    """
    desde ',/' para la izquierda solo permite 'positional arguments'
    desde '*,' hacia la derecha solo permite 'key word arguments'
    """
    print(a + b + c + d)


# calcular_resultado(1,2,3,4) # TypeError: calcular_resultado() takes 2 positional arguments but 4 were given

# calcular_resultado(1, 2, c=3, d=4) # devuelve: 10

"""-------------------"""

def operaciones(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a+b
    division = a/b
    return [suma,resta,multiplicacion,division]

print(operaciones(2,5)) # [7, -3, 7, 0.4]

for resultado in operaciones(2,5):
    print(resultado)