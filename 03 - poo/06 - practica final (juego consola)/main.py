import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input(
        "¡Bienvenido a la aventura en el Espacio! Por favor, ingresa tu nombre: "
    )
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15),
    ]

    enemigos_derrotados = []

    print("¡Comienza la aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("¿Que deseas hacer? ").lower()
            if accion == "atacar":
                danio_jugador = jugador.atacar()
                print(
                    f"Has atacado al {enemigo_actual.nombre} y la has causado {danio_jugador} de daño."
                )
                enemigo_actual.recibir_danio(danio_jugador)

                if enemigo_actual.salud > 0:
                    danio_enemigo = enemigo_actual.atacar()
                    print(
                        f"El {enemigo_actual.nombre} te atacó y te causó {danio_enemigo} de daño."
                    )
                    jugador.recibir_danio(danio_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate")
                break

        if jugador.salud <= 0:
            print("Has periddo la partida")
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)
        print(f"Salud actual: {jugador.salud} puntos")
        print(f"Nivel actual: {jugador.nivel}")
        print(f"Experiencia: {jugador.experiencia} puntos")

        continuar = input("Quieres seguir explorando? (s/n): ").lower()

        if continuar != "s":
            print("¡Gracias por haber jugado con nosotros!")
            break
    if not enemigos:
        print("¡Felicidades, has derrotado a todos los enemigos!")


# Nos aseguramos que solo podremos ejecutar este script desde el programa principal
if __name__ == "__main__":
    main()
