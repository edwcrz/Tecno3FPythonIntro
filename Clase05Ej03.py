## Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad
import os
print("Ingrese su nombre y edad para saber si es mayor de edad:")
try:
    nombre = str(input("Ingrese su nombre: "))
    nombre = nombre.strip()  # Eliminar espacios en blanco al inicio y al final
    nombre = nombre.capitalize()  # Asegurar que la primera letra del nombre esté en mayúscula
    edad = input("Ingrese su edad: ")
    edadentero = int(edad)
    if edadentero >= 18:
        print("{nombre}, usted es mayor de edad.".format(nombre=nombre))
    else:
        print("{nombre}, usted no es mayor de edad.".format(nombre=nombre))
except ValueError:
    os.system('cls')
    print("Error: El valor ingresado para la edad no es un numero entero.") 
