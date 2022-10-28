"""
Ejercicio: hacer un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Adivinar el número por parte del usuario

Usar una función para capitalizar el código común
"""

MIN = 0
MAX = 99

def solicitar_introducir_numero(invite):
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr)
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido

def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    """
    Esta función utiliza el anterior y añade una post-condición
    sobre los extremos del número a introducir
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        invite = "{} entre {} y {} incluídos".format(invite, minimum, maximum)
        datoIntroducido = solicitar_introducir_numero(invite)

        if minimum <= datoIntroducido <= maximum:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido


def jugar_tirada(numero, minimum, maximum):
    intento = solicitar_introducir_numero_extremo("Adivine el número", minimum, maximum)

    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimum = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximum = intento - 1
        victoria = False
    else:
        print("Victoria!")
        victoria = True
        minimum = maximum = intento
    return victoria, minimum, maximum


def decidir_extremos():
    while True:
        minimum = solicitar_introducir_numero("¿Cuál es el extremo mínimo ?")
        maximum = solicitar_introducir_numero("¿Cuál es el extremo máximo ?")
        if maximum > minimum:
            return minimum, maximum


def solicitar_introducir_el_numero_misterioso():
    return solicitar_introducir_numero_extremo("Introduzca el número a adivinar", minimum, maximum)


def jugar_una_partida(numero, minimum, maximum):
    while True:
        # Entramos en un bucle infinito
        # que permite jugar varios turnos

        victoria, minimum, maximum = jugar_tirada(numero, minimum, maximum)

        if (victoria):
            return


def jugar():
    minimum, maximum = decidir_extremos()
    numero = solicitar_introducir_el_numero_misterioso()
    jugar_una_partida(numero, minimum, maximum)


if __name__ == '__main__':
    print("El módulo se ejecuta")
    jugar()
else:
    print("El módulo se ha importado")

