# TRY, EXCEPT, FINALLY (manejo de errores)

# Manejo de la división por 0

a = 10
b = 0
# print(a/b) # falla 'ZeroDivisionError: division by zero'

a = 10
b = 5
resultado = 0

try:
    resultado = a / b  # auntque sean int devuelve float
    print(resultado)
except ZeroDivisionError: # si tiene un error lo maneja
    print("No se puede dividir por cero")
finally:
    resultado = 0

print(resultado)

#-------------------------------
