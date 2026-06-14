"""Crea una tupla con números, 
   pide un numero por teclado e 
   indica cuantas veces se repite."""

""" funcion contar_repetidos"""
def contar_repetidos (numero: int , numeros: tuple) -> int:
    contador_repetidos = 0
    for num in numeros:
        if numero == num:
            contador_repetidos +=1
    return contador_repetidos


""" bienvenida """
print("Bienvenido a programa del ejercicio 03")

""" creo una tupla"""
numeros : tuple = [4, 4 , 6, 4, 7, 2, 2, 6, 7, 0, 11, 7, 11]

while True:
    numero = input(print("ingrese un numero. Ingrese Exit para salir"))
    if numero == "Exit":
        print("Saliendo del programa. Ingresó Exit")
        break
    if not numero.isdigit():
        print ("no ingreso un numero. por favor ingrese un numero")
    else:
        repetidos = contar_repetidos(int(numero), numeros)
        print(f"el numero {numero} esta repetido {repetidos} veces")
