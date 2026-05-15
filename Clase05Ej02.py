## Realizar un programa que genere la tabla de multiplicar de un numero ingresado por el usuario (del 1 al 10)
try:
    numero = input("Ingrese un numero entero para generar su tabla de multiplicar: ")
    numeroentero = int(numero)
    print("Tabla de multiplicar del {numeroentero}:".format(numeroentero=numeroentero))
    for i in range(1, 11):
        resultado = numeroentero * i
        print("{numeroentero} x {i} = {resultado}".format(numeroentero=numeroentero, i=i, resultado=resultado))
except ValueError:   
    print("Error: El valor ingresado no es un numero entero.")