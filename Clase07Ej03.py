## Al iniciar se nos debe pedir ingresar un numero entero, 
# si este es distinto a 0 el programa inicia, 
# de lo contrario finaliza (tambien si se ingresa otra cosa que no sea un numero entero). 
# Se debe poder ingresar una Palabra o Frase y contar cuantos caracteres tiene dicha palabra o frase
# Con el valor obtenido en el punto anterior calcular su Factorial, una vez hecho esto , 
# decirnos si el resultado es par o impar. 
# Se deben imprimir los resultados por pantalla en cada paso. 
# Una vez cumplido esto, deberemos volver a pedir el ingreso de un número y realizar la verificación del punto 1

from math import factorial
print("Bienvenido al programa de conteo de caracteres y cálculo de factorial.")

#Hice algunos cambios para que verifiques lo que dijiste. Cualquier cosa podemos colaborar en otras oportunidades.
#La variable podria llamarse FLAG
Control = True
while Control:
    print("Ingrese un número entero para iniciar el programa (0 para finalizar): ")
    numero = input("Ingrese un numero entero: (ingrese 0 para finalizar) ")
    if not numero.isdigit():
        print("Error: El valor ingresado no es un numero entero. Programa finalizado.")
        Control = False
    else:
        numeroentero = int(numero)
        if numeroentero == 0:
            print("Programa finalizado porque ingresó 0.")
            Control = False
        else:
            frase = str(input("Ingrese una palabra o frase: "))
            cantidad_caracteres = len(frase)
            print(f"La cantidad de caracteres en la frase es: {cantidad_caracteres}")
            resultado_factorial = factorial(cantidad_caracteres)

            #cadena = f"El factorial de {cantidad_caracteres} es {resultado_factorial} y es " 
            #print(cadena + "par") if resultado_factorial % 2 == 0 else print(cadena + "impar")
            
            if resultado_factorial % 2 == 0:
                print(f"El factorial de {cantidad_caracteres} es {resultado_factorial} y es par.")
            else:
                print(f"El factorial de {cantidad_caracteres} es {resultado_factorial} y es impar.")
            # print("Ingrese un número entero para iniciar el programa (0 para finalizar): ")
            # numero = input("Ingrese un numero entero: (ingrese 0 para finalizar) ")

            
