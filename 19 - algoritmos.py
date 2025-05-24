# ALGORITMOS

# Serie de pasos secuenciales para poder resolver una problemática de forma eficiente

# -------------------------------
# Paso 1: Solicitar entrada al usuario.

edad = int(input("Por favor ingrese la edad del cliente: "))
# -------------------------------

# -------------------------------
# Paso 2: Verificar si la edad ingresada cumple con el requisito para entrar a la discoteca.

if edad >= 18:
    permitido = True
else:
    permitido = False
# -------------------------------

# -------------------------------
# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca.

if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, pero no se puede ingresar a la discoteca siendo menor de edad.")
# -------------------------------

# -------------------------------
# Código optimizado

edad = int(input("Por favor ingrese la edad del cliente: "))

if edad >= 18:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, pero no se puede ingresar a la discoteca siendo menor de edad.")
# -------------------------------

# -------------------------------
# Código optimizado V2

if int(input("Por favor ingrese la edad del cliente: ")) >= 18:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, pero no se puede ingresar a la discoteca siendo menor de edad.")
# -------------------------------
