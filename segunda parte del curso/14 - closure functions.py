# CLOSURE FUNCTIONS (CLAUSURAS)
# función interna hace referencia a variables locales de la función externa


def exterior(x):
    def interior(y):
        return x + y

    return interior


# Creamos una clausura llamando a la función EXTERIOR

clausura = exterior(10)

# Cuando llamemos a la función clausura va a RECORDAR el valor que le dimos a EXTERIOR

resultado = clausura(5)

""" 
def exterior(x = 10): # clausura
    def interior(y = 5): # resultado
        return x + y (10 + 5)

    return interior # 15
"""

print(resultado)
