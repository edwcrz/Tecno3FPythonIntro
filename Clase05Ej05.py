## Realizar un programa que sume los números ingresados por el usuario hasta que se ingrese un 0. 
## Al finalizar nos debe mostrar la suma por pantalla
from os import system
suma = 0
while True:
    try:
        numero = input("Ingrese un numero entero (0 para finalizar): ")
        numeroentero = int(numero)
        if numeroentero == 0:
            break
        suma += numeroentero
    except ValueError:
        system('cls')  # Limpia la pantalla (Windows)
        print("Error: El valor ingresado no es un numero entero.")
print("La suma de los numeros ingresados es: {suma}".format(suma=suma)) 
