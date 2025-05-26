import random


numero_secreto = random.randint(1, 100)
numero = 0
cantidad_intentos = 0
cantidad_max_intentos = 5
adivinado = False

print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado:
    if not cantidad_intentos < cantidad_max_intentos:
        print(
            "GAME OVER. No has adivinado el número secreto. El número secreto era: ",
            numero_secreto,
        )
        break
    
    numero = int(input("Introduce un número del 1 al 99: "))

    if numero == numero_secreto:
        print("¡Felicitaciones, has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")

    cantidad_intentos += 1
