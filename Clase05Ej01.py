## Realizar un programa que me diga si un numero es par o impar
from time import sleep
while True:     
    print ("Ingrese un numero para saber si es par o impar")
    try:
        numero = int(input("Ingrese un numero: "))
        
        if numero % 2 == 0:
            print("El numero ingresado es par.")
        else:
            print("El numero ingresado es impar.")
    
    except ValueError:
        print("Por favor, ingrese un numero valido.")
    sleep(2)