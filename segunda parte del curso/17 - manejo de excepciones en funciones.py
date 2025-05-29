# MANEJO DE EXCEPCIONES

# TRY/CATCH -> try / except

""" 
BEFORE
def division(dividendo, divisor):
    resultado = dividendo / divisor
    return resultado
"""

""" AFTER """
def division(dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("Error: no se puede dividir por ceto")
        resultado = None
    return resultado


print(division(5, 2))  # devuelve 2.5

print(division(5, 0))  # ZeroDivisionError: division by zero

print("Este mensaje es importantisimo")

"""
BEFORE
def obtener_entero(texto):
    entero = int(texto)
    return entero
"""

""" AFTER """
def obtener_entero(texto):
    try:
        entero = int(texto)
    except ValueError:
        print("Error: no es un número entero")
        entero = None
    return entero


print(obtener_entero("123")) # 123

print(obtener_entero("abc")) # ValueError: invalid literal for int() with base 10: 'abc'
