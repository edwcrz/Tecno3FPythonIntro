""" Crea una tupla con los meses del año, pide números al usuario, 
    si el numero esta entre 1 y la longitud máxima de la tupla, 
    muestra el contenido de esa posición 
    sino muestra un mensaje de error. 
    El programa termina cuando el usuario introduce un cero.
"""
""""fucion mes"""
def buscar_mes (num : int) -> str:
    return meses[num]

meses : tuple = []
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junip", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
# for mes in meses:
#    print (mes)

""" bienvenida """
print ("bienvenido al programa de meses del año")

""" pedir un numero al usuario """


while True:
    numero = input(print("ingrese un numero del 1 al 12: ,ingrese 0 para salir"))
    # print (f"el numero ingresado es {numero}")
    if not numero.isdigit():
        print("no ingresó un numero entero")
    elif int(numero) == 0:
        print ("salida del programa. Ingreso 0")
        break
    elif int(numero) <= 0 or int(numero) > 12:
        print("ingreso un numero fuera de los numeros especificados")
    else :
        indice = int(numero)-1
        mes_encontrado = buscar_mes(indice)
        print (f"el mes que ha ingresado es {mes_encontrado}")
        
