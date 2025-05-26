# FUNCIONES
"""
Bloque de código reutilizable que realiza una tarea específica. Las funciones permiten dividir un programa en partes más pequeñas y manejables, lo que facilita la lectura, la depuración y la reutilización del código.
"""

# SINTAXIS BÁSICA


def nombre_funcion(parametros):
    """Docstring de la función"""
    # Cuerpo de la función
    # Puede contener una o más líneas de código
    return "resultado"

""" 
.1 def: palabra clave que indica el inicio de la definición de la función.
.2 nombre_funcion: nombre que le damos a la función. Debe seguir las reglas de nombrado de variables de Python 
    ('/primera parte del curso/03 - variables.py')
.3 parametros: son las variables que la función espera recibir cuando es llamada -> pueden ser opcionales
.4 '''Docstring de la función''': es un comentario de cadena (docstring) que describe brevemente la función y su funcionalidad. Es opcional, pero es una buena práctica incluirlo para documentar nuestras funciones.
.5 return resultado: la instrucción return indica el valor que la función devuelve cuando es llamada. Es opcional y puede devolver cualquier tipo de objeto, o incluso no devolver nada.
"""

# -------------------------------
'''-------------------'''
# -------------------------------

# PARÁMETROS vs ARGUMENTOS

""" 
Los parámetros son variables declaradas en la definición de la función que sirven como marcadores de posición para los valores que se pasan a la función cuando es llamada.

Los argumentos son los valores reales que se pasan a la función cuando es llamada. Estos valores se asignan a los parámetros correspondientes de la función.
"""

# a y b son los parámetros (variable)
def suma(a,b):
    """Esta función suma dos números."""
    resultado = a+b
    return resultado

# 3 y 5 son los argumentos (valores)
resultado_suma = suma(3,5)
print(resultado_suma) # Devuelve: 8