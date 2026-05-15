## Realizar un programa donde el usuario ingrese una palabra y un numero e 
## imprima por pantalla la palabra ingresa tantas veces como el numero ingresado
try:
    palabra = str(input("Ingrese una palabra: "))
    numero = input("Ingrese un numero entero: ")
    numeroentero = int(numero)
    resultado = palabra * numeroentero
    print("La palabra '{palabra}' repetida {numeroentero} veces es: {resultado}".format(palabra=palabra, numeroentero=numeroentero, resultado=resultado))
except ValueError:
    print("Error: El valor ingresado para el numero no es un numero entero.") 
    