"""
Conversi�n a un entero y comparaci�n

(probar con un dato introducido que no es un n�mero)
"""

# Primer n�mero
numero1 = input("Introduzca un primer n�mero: ")
numero1 = int(numero1)

# Segundo n�mero
numero2 = int(input("Introduzca un segundo n�mero: "))

# Hacer la comparaci�n
comparacion = numero1 < numero2

print(numero1, "<", numero2, ":", comparacion)

