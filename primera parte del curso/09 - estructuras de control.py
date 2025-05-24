# ESTRUCTURAS DE CONTROL

"""Bloque de código que permite controlar el flujo d eejecución de un programa.
Estas estructuras determinan qué instrucciones se ejecutarán y en qué orden,
basándose en condiciones específicas."""

""" Estructuras de decisión (condicionales): permiten ejecutar cierto bloque de código si se cumple una condición, 
de lo contrario, se ejecuta otro bloque de código"""

""" Bucles (loops): permiten ejecutar un bloque de código repetidamente mientras de cumpla una condición,
o hasta que una condición de vuelva falsa."""

""" Estructuras de control de excepciones: permiten manejar errores y excepciones en un programa, 
controlando cómo se manejan los errores cuando ocurren durante la ejecución."""

# CONDICIONALES

""" 
if condicion_1:
    # código a ejecutar si la condicion_1 es verdadera
elif condicion_2:
    # código a ejecutar si la condicion_2 es verdadera
else:
    # código a ejecutar si ninguna de las condiciones anteriores es verdadera
"""

# CONDICIONALES TERNARIAS

""" 
Forma concisa de expresar una estructura condicional en una sola línea de código.
Se utilizan principalmente para asignar valores a una variable en función de una condición
"""

# valor_si_condicion_verdadera if condicion else valor_si_condicion_falsa

x = 10
resultado = "positivo" if x > 0 else "negativo"

# print(resultado)

# BUCLES

"""
Estructuras d econtrol que permiten ejecutar repetidamente un bloque de código 
mientras se cumpla una condición o hasta que una condición se vuelva falsa
"""

# Bucle WHILE
"""
        while condicion:
            # código a ejecutar mientras la condición sea verdadera

    """

# Bucle FOR
""" 
        for indice in range(cantidad):
            # código a ejecutar en cada iteración
            
    """

# MANEJO DE EXCEPCIONES

""" 
Permiten manejar errores y excepciones que pueden ocurrir durante la ejecución de un programa
"""

""" 
    try: 
        # código que puede generar una excepción
    except TipoDeExcepcion as nombre_variable
        # código para manejar la excepción
    finally:
        # código que siempre se ejecuta, OPCIONAL

"""

# PALABRAS CLAVE

""" Forman parte del conjunto de herramientas que Python proporciona para controlar el flujo de ejecución y la lógica del programa."""

# BREAK

for i in range(5):
    if i == 3:
        break # Termina acá, no sigue
    # print(i)  # Se espera: 0,1,2

    # CONTINUE
for i in range(5):
    if i == 3:
        continue # Saltea el valor, pero sigue hasta el final
    # print(i)  # Se espera: 0,1,2,4

    # PASS

x = 10
if x > 5:
    pass  # No hace nada, solo sirve como marcador de posición
else:
    x=0
    # print("x es menor o igual a 5")

x = 5
if x > 5:
    pass  # No hace nada, solo sirve como marcador de posición
else:
    x=0
    # print("x es menor o igual a 5")

# -------------------------------
