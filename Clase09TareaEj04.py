## Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el usuario
from typing import List, Tuple, Dict, Set
from math import sqrt, pow, pi, sin, cos, tan, log, exp
 import matplotlib.pyplot as plt


def dibujar_rectangulo(filas: int, columnas: int) -> None:
    for i in range(filas):
        for j in range(columnas):
            print("*", end="")
        print()  # Salto de línea después de cada fila
        plt.title("Coordenada (i,j)")
        plt.grid(True)
        plt.plot(j, i, 'ro')  # Dibuja un punto rojo en la coordenada (j, i)

plt.show()

## bienvenido al programa de dibujo de rectángulos
print("Bienvenido al programa de dibujo de rectángulos")

try: fila = int(input("Ingrese el número de filas: "))
except ValueError:
    print("Error: El valor ingresado no es un número entero.")
    fila = 0

try: columna = int(input("Ingrese el número de columnas: "))
except ValueError:
    print("Error: El valor ingresado no es un número entero.")
    columna = 0

dibujar_rectangulo(fila, columna)