import random

CARAS_DADO = 6
CANTIDAD_DADOS = 2


def simular_tirada(puntaje_objetivo, nombre_jugador):
    """Simula el tiro de dos dados y evalua si su suma
    supera el puntaje meta.
    """
    dado_uno = random.randint(1, CARAS_DADO)
    dado_dos = random.randint(1, CARAS_DADO)
    puntaje_total = dado_uno + dado_dos

    if puntaje_total >= puntaje_objetivo:
        mensaje = (
            f"Felicidades {nombre_jugador}, tus dados sumaron "
            f"{puntaje_total} y alcanzaste la meta!"
        )
        print(mensaje)
    else:
        mensaje = (
            f"Mala suerte {nombre_jugador}, solo sumaste "
            f"{puntaje_total} puntos."
        )
        print(mensaje)

    return puntaje_total


nombre = input("Ingrese el nombre del jugador: ")
meta_objetivo = int(input("Cual es el numero meta que deseas alcanzar?: "))

resultado_final = simular_tirada(meta_objetivo, nombre)
print(resultado_final)