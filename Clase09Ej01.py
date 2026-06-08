## funciones
## los procesos son funciones que no retornan un valor, solo realizan una acción
## las funciones son procesos que retornan un valor, es decir, realizan una acción y devuelven un resultado
## varialble type hint, float, str, bool, list, tuple, dict, set
## anotaciòn de ayuda de variables, def nombre_funcion(parametro1: tipo, parametro2: tipo) -> tipo:
## para declarar una constante se puede usar mayusculas, aunque no es obligatorio, es una convención, por ejemplo: PI = 3.14
## para declarar una constante del tipo PI se usa from typing import import final, PI: final = 3.14
from typing import final



a = int | float
b = int | float
c = int | float 

def restar(a: int | float, b: int | float = 1, c: int | float = 0) -> tuple[int | float, int | float]:
    """
    esta función resta dos números y luego resta el resultado con un tercer número, 
    ambos parámetros son opcionales, si no se ingresan se toman los valores por defecto
    esto permite documentar la función y facilitar su uso, además de mejorar la legibilidad del código
    documentar es importante para entender el propósito de la función, los parámetros que recibe y el valor que retorna,
    esto es especialmente útil cuando se trabaja en equipo o cuando se vuelve a revisar el código después de un tiempo,
    ya que permite entender rápidamente lo que hace la función sin tener que leer todo el código.
    trae un comentario en bloque que se llama docstring, que es una cadena de texto 
    que se coloca justo debajo de la definición de la función,
    y que se utiliza para documentar la función, es decir, para explicar qué hace la función,
    cuáles son sus parámetros, qué valor retorna, etc.
    doc string es una convención en Python para documentar funciones, clases y módulos, y se puede acceder a ella a través del atributo __doc__ de la función, clase o módulo.
    doc string es una herramienta muy útil para mejorar la legibilidad y mantenibilidad del código, ya que permite entender rápidamente lo que hace una función, clase o módulo sin tener que leer todo el código.
    doc string es una buena práctica de programación, ya que permite documentar el código de manera clara y concisa, lo que facilita su uso y mantenimiento a largo plazo.
    doc string debe ser resumidoo, claro y conciso, y debe explicar qué hace la función, cuáles son sus parámetros, qué valor retorna, etc.
    doc string debe ser escrita en tercera persona, es decir, debe describir lo que hace
    """
    print (F"El resultado de restar {a} - {b} es: {a - b}")
    return a - b, a - c

resultado = restar(a = 9, b = 2, c = 3)
print(resultado)
print(type(resultado))
resultado1 , resultado2 = restar(a = 9)
print(resultado1)
print(resultado2)
print(type(resultado1))
print(type(resultado2))
print(restar.__doc__)
print(restar.__annotations__)
help(restar)
## help trae las anotaciones y las annotations traen la documentación de la función, es decir, el docstring, además de las anotaciones de tipo de los parámetros y el valor de retorno.
print (restar.__name__)
