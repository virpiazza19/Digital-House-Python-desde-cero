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
"""-------------------"""
# -------------------------------

# PARÁMETROS vs ARGUMENTOS

""" 
Los parámetros son variables declaradas en la definición de la función que sirven como marcadores de posición para los valores que se pasan a la función cuando es llamada.

Los argumentos son los valores reales que se pasan a la función cuando es llamada. Estos valores se asignan a los parámetros correspondientes de la función.
"""


# a y b son los parámetros (variable)
def suma(a, b):
    """Esta función suma dos números."""
    resultado = a + b
    return resultado


# 3 y 5 son los argumentos (valores)
resultado_suma = suma(3, 5)
## print(resultado_suma)  # Devuelve: 8


""" CONSIDERACIONES

-> El valor devuelto por una función se especifica mediante la instrucción RETURN.

-> Una función puede devolver cualquier tipo de objeto, o incluso no devolver nada.

-> El valor devuelto por una función puede ser asignado a una variable o utilizado directametne en otra expresión.

-> Una función puede tener múltiples parámetros, tanto obligatorios como opcionales.

-> Los parámetros pueden tener valores predeterminados, lo que los convierte en parámetros opcionales.

-> Una función puede devolver múltiples valores utilizando tuplas o estructuras de datos más complejas.

"""


def greetings(
    name, greeting="Hi"
):  # En este caso el 2do parámetro es opcional ya que tiene un valor predefino
    """This function shows a personalize message."""
    message = f"{greeting}, {name}!"
    return message


# Llamado a la función solo con el argumento opcional
## print(greetings("Juan")) # Devuelve 'Hi, Juan!'

# Llamado a la función con dos argumentos
## print(greetings("Virginia","Good morning")) # Devuelve 'Good morning, Virginia!'

# -------------------------------
"""-------------------"""
# -------------------------------

# SCOPE y NAMESPACES

""" ALCANCE (scope) -> el alcance de una variable se refiere a la aprte del programa en la que la variable es accesible. En Python, el alcance determina dónde en el código una variable puede ser utilizada o referenciada. El alcance de una varaible está influenciada por dónde y cómo se define la variable en el código.

    -> Alcance LOCAL: las variables definidas dentro de una función tienen un alcance local. Estas variables solo son accesibles dentro de la función en la que se definne. Una vez que la función termina de ejecutarse, las variables locales se eliminan de la memoria.

    -> Alcance GLOBAL: las variables definidas fuera de todas las funciones, es decir, en el nivel superior del script, tienen un alcance global. Estas variables son accesibles desde cualquier parte del código, incluídas las funciones. Sin embargo, es posible acceder a variables globales dentro de una función utilizando la palabra clave 'global'.
"""

""" NAMESPACE -> un espacio de nombres (namespace) en Python es un contenedor que mapea nombres a objetos en el propio programa. Cada espacio de nombres tiene su propio alcance y contiene los nombres de las variables y sus respectivos objetos. Python utiliza varios espacios de nombres, incluídos el espacio de nombre global (módulo) y los espacios de nombres locales (funciones).
"""

global_var = 10  # variable global


def mi_funcion():
    local_var = 20  # variable local
    print(
        "Variable local dentro de la función:", local_var
    )  # devuelve: 'Variable local dentro de la función: 20'
    print(
        "Variable global dentro de la función:", global_var
    )  # devuelve: 'Variable global dentro de la función: 10'


mi_funcion()
print(
    "Variable global fuera de la función:", global_var
)  # devuelve: 'Variable global fuera de la función: 10'
