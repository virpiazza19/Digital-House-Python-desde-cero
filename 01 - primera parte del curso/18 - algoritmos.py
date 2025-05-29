import math

# ALGORITMOS

# Serie de pasos secuenciales para poder resolver una problemática de forma eficiente

# -------------------------------
# Paso 1: Solicitar entrada al usuario.

radio = float(input("Por favor ingrese una palabra: "))
# -------------------------------

# -------------------------------
# Paso 2: Calcular el área del círculo utilizando la fórmula área = π * radio^2.

area = math.pi * (radio ** 2)
# -------------------------------

# -------------------------------
# Paso 3: Mostrar al usuario el resultado.

print("El área del círculo con radio", radio, "es:", area)
# -------------------------------

# -------------------------------
# Código optimizado

area = math.pi * (float(input("Por favor ingrese una palabra: ")) ** 2)

print("El área del círculo con radio", radio, "es:", area)

# -------------------------------
