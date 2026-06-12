## Cree una funcion que calcule el promedio de N notas

def acumular(notas: list) -> float:
    total = 0
    for i in range(len(notas)):
        notas[i] = float(notas[i])
        total += notas[i]
    return total

def contar(notas: list) -> int:
    cantidad = len(notas)
    return cantidad

def promediar(notas: list) -> float:
    acumulado = acumular(notas)
    cantidad = contar(notas)
    promedio = acumulado / cantidad
    return promedio

# declaracion de variables 
control = True
nota: int = 0
notas = []
# indicaciones al usuario
print ("bienvenido al programa de calculo de promedio de notas")
print ("ingrese las notas de a una, ingrese -1 para salir")

while not nota == "-1" and control:
    try: 
        nota = int(input(print("ingrese una nota: ")))
    except ValueError:
        print ("ingreso inválido. Asegúrese de ingresar un número positivo o -1 para salir.")
    notas.append(nota)
    if nota == -1:
        control = False
        notas.pop()  # Eliminar el -1 de la lista de notas  
print (f"las notas ingresadas son: {notas}")
promedio = promediar(notas)
print (f"el promedio de las notas ingresadas es: {promedio}")