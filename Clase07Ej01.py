## el juego termina cuando el jugador adivina el numero secreto o realizo 5 intentos
## cuando se pide ingresar el numero se le debe indicar al jugador el rango maximo y minimo del numero secreto
## el numero secreto se genera de forma aleatoria cada vez que se inicia el juego
## si el jugador falla se debe informar si el numero secreto es mayor o menor al numero ingresado por el jugador
## al finalizar el juego se debe mostrar un mensaje indicando si el jugador gano o perdio y cual era el numero secreto
import random
from random import randint
numero_secreto = random.randint(1, 50)
intentos = 0
max_intentos = 5
control = True

print("Bienvenido al juego de adivinanza!")
print("Tienes que adivinar un número entre 1 y 50.")
print(f"Tienes {max_intentos} intentos.")

while control and intentos < max_intentos:
    try:
        numero_ingresado = (input("Ingrese un número entre 1 y 50: "))
        if not numero_ingresado.isdigit():
            raise ValueError("El valor ingresado no es un número válido.")  
        numero_ingresado = int(numero_ingresado)
        if numero_ingresado >= 1 and numero_ingresado <= 50:
            intentos += 1
            if numero_ingresado == numero_secreto:
                print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
                control = False
                break
            elif numero_ingresado < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")

            if intentos == max_intentos:
                print(f"Lo siento, has agotado tus intentos. El número secreto era: {numero_secreto}")
                control = False

        else:
            print("Error: Por favor, ingrese un número válido.")    
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")    