## Realizar un programa que le pida al usuario un numero y le sume 5, el resultado debe mostrarce por pantalla
try:
    numero = input("Ingrese un numero entero: ")
    numeroentero = int(numero)
    resultado = numeroentero + 5
    print("El resultado de la suma es: {resultado}".format(resultado=resultado))
except ValueError:
    print("Error: El valor ingresado no es un numero entero.")