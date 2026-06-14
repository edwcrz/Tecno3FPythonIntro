"""import sys, os, random, subprocess

def limpiar_pantalla():
    # Detecta el sistema operativo
    comando = "cls" if os.name == "nt" else "clear" # esto es un ternario, lo veremos el proximo cuatri

    # Ejecuta el comando de forma segura
    subprocess.run([comando], shell=True)


numero_random = random.randrange(1000, 9999) #con esto crean un numero random
 
os.path.isfile(ruta) # la palabra ruta obtendra el nombre del archivo y verificara que exista

sys.exit() #con este comando cierra la ejecucion del programa
"""
"""Bienvenido al programa de Tickets"""
print ("Bienvenido al programa de gestión de tickets")

""" inicializo funciones"""
def alta_ticket ():
    return

def mostar_ticket():
    return

def leer_ticket ():
    return

def salir ():
    return

# funcion controlar que no haya caracteres especiales en un strint
def controlar_caracteres_especiales(texto: str, caracteres_especiales: tuple) -> bool:
    encontrado : bool = False
    texto = list()
    texto_list = list(texto)
    for caracter in texto_list:
        for char_especial in caracteres_especiales:
            if caracter == char_especial:
                encontrado = True
                return encontrado

def normalizar_string(texto):
    try:
        return int(texto)
    except ValueError:
        try:
            return float(texto)
        except ValueError:
            return str(texto)

def control_ingreso_string (texto) -> tuple[str, bool]:
    salir : bool = False
    if texto == "exit":
        salir = True
   #     break
    elif texto.strip() == "":
        print("Ingreso no válido, no se permiten entradas vacías. ingrese nuevamente.")
        salir = True
    #    continue
    if texto.find(".") and texto.replace(".","").isdigit():
        print("Ingreso no válido, ingresó un número decimal. ingrese nuevamente")
        salir = True
    #    continue
    elif texto.find(",") and texto.replace(",","").isdigit():
        print("Ingreso no válido, ingresó un número separado por comas. ingrese nuevamente")
        salir = True
    #    continue
    elif texto.isdigit():
        print(".Ingresó un número entero. ingrese nuevamente")
        salir = True
    #    continue
    elif controlar_caracteres_especiales(texto, caracteres_especiales):
        print("Ingreso no válido, ingresó un caracter especial. Ingrese nuevamente.")
        salir = True
    #    continue
    elif isinstance(normalizar_string(texto), str):
        salir = True
    #    break
    else:
        print ("error de ingreso. ingrese un nombre")
        salir = True
    #    break
    return texto, salir


""" inicializo variables"""
tickets : list = []
print(type(tickets))
ticket : dict[str:str, str:str, str:str, str:str]= {}
print(type(ticket))

caracteres_especiales : tuple = ()
caracteres_especiales = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?")



ticket = {
            "numero_ticket":"999",
            "nombre":"prueba",
            "sector":"grip",
            "asunto":"BGP unreachable",
            "problema":"la sesion BGP con le peer 209.217.24.13 se encuntra unreachable",
         }

for clave, valor in ticket.items():
    print(f"imprimo clave : valor {clave}:{valor}")


tickets.append(ticket)
print(tickets)
salir = False

while not salir:
    print("Ingrese un ticket siguiendo los proximos 4 pasos. Exit para salir")
    nombre_ingresado = input("ingrese el nombre de la persona que genera el ticket :")
    print(f"el nombre ingresado es {nombre_ingresado}")
    nombre_ingresado_validado, salir = control_ingreso_string (nombre_ingresado)
    print(type(nombre_ingresado_validado))
    print(f"el nombre ingresado es : {nombre_ingresado_validado}")
print ("fin del programa")
