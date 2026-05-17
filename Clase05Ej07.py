## Realizar un programa que pida al usuario su edad y nos diga si debe votar, y en caso de tener entre 16 y 18. 
# preguntar al usuario si decide votar o no
from os import system
print("Ingrese su edad:")
try:
    edad = int(input())
    if edad >= 18:
        print("Usted debe votar.")
    elif 16 <= edad < 18:
        print("Usted tiene la opción de votar, presentarse a votar es su elección, decide votar? (si/no)")
        respuesta = input().lower()
        if respuesta == "si":
            print("Usted ha decidido votar.")
        elif respuesta == "no":
            print("Usted ha decidido no votar.")
        else:
            print("Respuesta no válida. Por favor, responda con 'si' o 'no'.")
    else:
        print("Usted no tiene edad para votar.")
except ValueError:
    system('cls')
    print("Error: El valor ingresado para la edad no es un número entero.")