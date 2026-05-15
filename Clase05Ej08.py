## Realizar un programa que pida al usuario que ingrese varios números y que devuelva la suma del cuadrado de esos números
print("Ingrese varios numeros para calcular la suma de sus cuadrados (ingrese 0 para finalizar):")
suma_cuadrados = 0
while True:
    try:
        numero = input("Ingrese un numero (0 para finalizar): ")
        numeroentero = int(numero)
        if numeroentero == 0:
            break
        suma_cuadrados += numeroentero ** 2
    except ValueError:
        print("Error: El valor ingresado no es un numero entero.")
print("La suma de los cuadrados de los numeros ingresados es: {suma_cuadrados}".format(suma_cuadrados=suma_cuadrados)) 