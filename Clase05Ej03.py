## Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad
print("Ingrese su nombre y edad para saber si es mayor de edad:")
try:
    nombre = str(input("Ingrese su nombre: "))
    edad = input("Ingrese su edad: ")
    edadentero = int(edad)
    if edadentero >= 18:
        print("}, usted es mayor de edad.".format(nombre=nombre))
    else:
        print("Hola {nombre}, usted no es mayor de edad.".format(nombre=nombre))
except ValueError:
    print("Error: El valor ingresado para la edad no es un numero entero.") 
