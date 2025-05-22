nombre_1 = input("¿Cómo se llamará el jugador 1?: ")
nombre_2 = input("¿Cómo se llamará el jugador 2?: ")

cantidad_maxima_aciertos = 3
aciertos_jugador_1 = 0
aciertos_jugador_2 = 0

while (
    aciertos_jugador_1 < cantidad_maxima_aciertos
    and aciertos_jugador_2 < cantidad_maxima_aciertos
):
    # Refactorización: modificamos el código para que sea legible, haya más líneas de código, sea más eficiente.
    jugador_1 = input(nombre_1 + " ¿Qué elegís?: piedra, papel o tijera?: ").lower()
    jugador_2 = input(nombre_2 + " ¿Qué elegís?: piedra, papel o tijera?: ").lower()
    condicion = (
        (jugador_1 == "piedra" and jugador_2 == "tijera")
        or (jugador_1 == "papel" and jugador_2 == "piedra")
        or (jugador_1 == "tijera" and jugador_2 == "papel")
    )

    if jugador_1 == jugador_2:
        print("¡Ha sido un empate!")
    elif condicion:
        print(nombre_1, "ha sumado un punto")
        aciertos_jugador_1 += 1
    else:
        print(nombre_2, "ha sumado un punto")
        aciertos_jugador_2 += 1

    print("Puntajes hasta el momento:")
    print(nombre_1, ":", aciertos_jugador_1)
    print(nombre_2, ":", aciertos_jugador_2)

if aciertos_jugador_1 == cantidad_maxima_aciertos:
    print("¡Ha ganado", nombre_1, "!")
else:
    print("¡Ha ganado", nombre_2, "!")
