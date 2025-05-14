# IF, ELIF, ELSE

x = -3
if x > 0:
    print("X es un número positivo")
elif x < 0:
    print("X es un número negativo")
else:
    print("X es igual a 0")

# -------------------------------

visa = False
pasaporte = True

if visa and pasaporte:  # Multiples condiciones
    print("Puedes ingresar a cualquier país de destino")
elif pasaporte and not visa:
    print("Puedes ingresar a los países que no requieren visa")
else:
    print("Debes conseguir la documentación antes de viajar")


#-------------------------------

edad = 40

if edad < 18 or edad > 60:
    if edad < 18:
        print("No tienes edad suficiente para entrar a la disco")
    else:
        print("Por una cuestión de seguridad no se permite el ingreso a mayores de 60")
elif edad >= 18 and edad <= 60:
    print("Puedes ingresar a la disco")
