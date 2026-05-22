## al iniciar se nos debe pedir ingresar un numero entero, si es distino a cero inicia sino debe fnalizar el programa, 
## se debe poder ingresar una palabra o frase y contar los caracteres que tiene, luego se debe mostrar el resultado por pantalla
## se debe sacar el factorial de la cantidad de caracteres e informar si es par o impora y mostrar el resultado por pantalla 
## se debe imprimir el resultado del factorial con un mensaje que indique si es par o impar
from math import factorial 
try:
    numero = input("Ingrese un numero entero (0 para finalizar): ")
    numeroentero = int(numero)
    if numeroentero == 0:
        print("Programa finalizado.")
    else:
        frase = str(input("Ingrese una palabra o frase: "))
        cantidad_caracteres = len(frase)
        print(f"La cantidad de caracteres en la frase es: {cantidad_caracteres}")
        
        resultado_factorial = factorial(cantidad_caracteres)
        if resultado_factorial % 2 == 0:
            print(f"El factorial de {cantidad_caracteres} es {resultado_factorial} y es par.")
        else:
            print(f"El factorial de {cantidad_caracteres} es {resultado_factorial} y es impar.")