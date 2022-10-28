"""
Ejercicio: hacer un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Adivinar el número por parte del usuario

Usar una función para capitalizar el código común
"""

MIN = 0
MAX = 99


def solicitar_introducir_numero(invite, minimum=MIN, maximum=MAX):
    # Completar la entrada:
    invite += " entre " + str(minimum) + " y " + str(maximum) + " incluídos: "

    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = input(invite)

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            pass
        else:
            # Hacer la comparación
            if minimum <= datoIntroducido <= maximum:
                # Tenemos lo que queremos, salimos del bucle
                break
    return datoIntroducido


# PARTE 1
numero = solicitar_introducir_numero("Introduzca el número a adivinar")

minimum = MIN
maximum = MAX

# PARTE 2
while True:
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    intento = solicitar_introducir_numero("Adivine el número", minimum, maximum)

    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimum = intento + 1
    elif intento > numero:
        print("Demasiado grande")
        maximum = intento - 1
    else:
        print("Victoria!")
        break

