# BREAK, CONTINUE, PASS (palabras clave)

# BREAK

contador = 0
prohibido = 23

while contador < 25:
    # print(contador)
    if contador == prohibido:
        break  # corta la ejecución del programa cuando la condición es verdadera
    contador += 1

# -------------------------------

# CONTINUE

contador = 0
prohibido = 23

"""while contador < 25:
    print(contador)
    if contador == prohibido:
        continue  # cuando la condición es verdadera saltea el bucle y el código que le sigue
    contador += 1 # esta condición debería estar arriba de la condición ya que puede crear bucles infinitos
"""
while contador < 25:
    contador += 1  # esta condición está arriba de la condición para evitar bucles infinitos
    if contador == prohibido:
        continue  # cuando la condición es verdadera saltea el bucle y el código que le sigue
    # print(contador)

for i in range(10):
    if i % 2 == 0:
        continue
    # print(i)


# -------------------------------

# PASS

edad = 18

if edad > 18:
    print("Puedes ingresar a esta institución")
elif edad == 18:
    pass
else:
    print("No tienes edad suficiente para entrar aquí")

# -------------------------------
