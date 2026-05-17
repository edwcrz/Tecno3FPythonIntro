## Realizar un programa que pide al usuario su nombre y apellido y 
# en el caso de no estar la primera letra en mayúscula devolver el mismo nombre y apellido pero con la primer letra en mayúscula
from os import system
nombre = str(input("Ingrese su nombre: "))
nombre = nombre.strip()  # Eliminar espacios en blanco al inicio y al final
apellido = str(input("Ingrese su apellido: "))
apellido = apellido.strip()  # Eliminar espacios en blanco al inicio y al final
try:
    if not nombre[0].isupper() or not apellido[0].isupper():
        nombre = nombre.capitalize()
        apellido = apellido.capitalize()
    print("Su nombre y apellido es: {nombre} {apellido}".format(nombre=nombre, apellido=apellido))
except IndexError:
    system('cls')
    print("Error: El nombre o apellido ingresado está vacío.")