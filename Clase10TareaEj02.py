""" Pide números y mételos en una lista, 
    cuando el usuario meta un 0 ya dejaremos de insertar. 
    Por último, muestra los números ordenados de menor a mayor."""

"""Bienvenida"""
print ("Bienvenido al programa para ordenar numeros")

numeros : list = []
# print(type(numeros))

while True:
    numero = input(print("ingrese un numero, ingrese 0 para salir"))    

    if not numero.isdigit():
        print("no ingresó un número. Por favor ingrese un número")
    elif int(numero) == 0:
        print("saliendo del programa. ingresó un 0")
        break
    else :
        numeros.append(int(numero))
numeros.sort()
print(f"los numeros ingresados son {numeros}")

