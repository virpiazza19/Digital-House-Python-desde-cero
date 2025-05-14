# WHILE

# Mientras se cumple una condición

contador = 0

while contador < 5:
    # print("El contador es:", contador) # Arranca con el valor original de la variable, que es 0
    contador += 1

# print("El contador final es:", contador)

#-------------------------------

contador = 0

while contador < 5:
    contador += 1
    # print("El contador es:", contador) # Arranca con el valor modificado, que es 1

# print("El contador final es:", contador)

#-------------------------------

contador = 0
limite = 5
sumatoria = 0

while contador <= limite:
    sumatoria += contador
    contador += 1

print("La suma de los números hasta:", limite,"es:", sumatoria)

#-------------------------------