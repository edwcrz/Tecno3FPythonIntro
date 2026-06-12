## Cree una funcion que determine que numero de una serie de N numeros es mayor

def determinar_mayor(numeros: list) -> int:
    mayor = numeros[0]
    for n in numeros:
        if n > mayor:
            mayor = n
    return mayor

print ("bienvenido al programa de calculo de numero mayor de una serie de numeros")
print ("ingrese las numeros de a una, ingrese -1 para salir") 
numeros = []
control = True
numero: int = 0
while not numero == "-1" and control:
    try: 
        numero = input(print("ingrese un numero: "))
    except ValueError:
        print ("ingreso inválido. Asegúrese de ingresar un número entero o -1 para salir.")
    numeros.append(numero)
    if numero == -1:
        control = False
        numeros.pop()  # Eliminar el -1 de la lista de números


mayor_numero = determinar_mayor(numeros)
print(f"El número mayor de la serie es: {mayor_numero}")