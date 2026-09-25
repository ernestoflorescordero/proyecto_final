import random

# configuracion inicial
caras_dado = 6
l = 2


def simularTirada(puntajeObjetivo, nombreJugadorQueParticipaEnLaRondaActual):
    # print("Lanzando dados a la mesa...")
    d1 = random.randint(1, caras_dado)
    d2 = random.randint(1, caras_dado)
    tot = d1 + d2

    # Evaluacion de resultado
    if tot >= puntajeObjetivo:
        print("Felicidades " + nombreJugadorQueParticipaEnLaRondaActual + ", tus dados sumaron " + str(tot) + " y alcanzaste la meta!")
    else:
        # print("No alcanzo los puntos necesarios")
        print("Mala suerte " + nombreJugadorQueParticipaEnLaRondaActual + ", solo sumaste " + str(tot) + " puntos.")

    return tot


# Flujo principal interactivo
n = input("Ingrese el nombre del jugador: ")
meta = int(input("Cual es el numero meta que deseas alcanzar (2 al 12)?: "))
resultado = simularTirada(meta, n)
print(resultado)