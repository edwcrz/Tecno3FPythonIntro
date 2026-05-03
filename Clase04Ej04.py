## Ingresar 5 numeros y calcular su promedio, el resultado mostrarlo por pantalla
try:
    print("Ingrese 5 numeros para calcular su promedio:")
    numero1 = input("Ingrese el primer numero: ")
    numero2 = input("Ingrese el segundo numero: ")
    numero3 = input("Ingrese el tercer numero: ")
    numero4 = input("Ingrese el cuarto numero: ")
    numero5 = input("Ingrese el quinto numero: ")

    numero1entero = int(numero1)
    numero2entero = int(numero2)
    numero3entero = int(numero3)
    numero4entero = int(numero4)
    numero5entero = int(numero5)

    promedio = (numero1entero + numero2entero + numero3entero + numero4entero + numero5entero) / 5
    promedio = float(round(promedio, 2))  # Redondear el promedio a 2 decimales
    print("El promedio de los numeros ingresados es: {promedio}".format(promedio=promedio))
except ValueError:
    print("Error: Uno o mas de los valores ingresados no son numeros enteros.") 