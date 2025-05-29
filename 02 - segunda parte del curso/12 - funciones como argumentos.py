# FUNCIONES COMO ARGUMENTOS

# Callbacks -> función por argumento de otra función para que resuelve algo puntual

def aplicar_funcion(func,valor):
    return func(valor)

def cuadrado(x):
    return x*x

def cubo(x):
    return x*x*x

print(aplicar_funcion(cuadrado,3)) # Devuelve 9

print(aplicar_funcion(cubo,3)) # Devuelve 27

