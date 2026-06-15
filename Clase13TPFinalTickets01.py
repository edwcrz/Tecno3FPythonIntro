from random import randint

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
            texto = str(texto)
            texto = texto.strip()
            return texto

def control_ingreso_string (texto) -> tuple[str, bool, bool]:
    salir : bool = False
    error_verificacion_string : bool = False
    if texto.strip().lower() == "exit":
        salir = True
   #     break
    elif texto.strip() == "":
        print("Ingreso no válido, no se permiten entradas vacías. ingrese nuevamente.")
        error_verificacion_string = True
    #    continue
    elif not texto.find(".") == -1 and texto.replace(".","").isdigit():
        print("Ingreso no válido, ingresó un número decimal. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif not texto.find(",") == -1 and texto.replace(",","").isdigit():
        print("Ingreso no válido, ingresó un número separado por comas. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif texto.isdigit():
        print(".Ingresó un número entero. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif controlar_caracteres_especiales(texto, caracteres_especiales):
        print("Ingreso no válido, ingresó un caracter especial. Ingrese nuevamente.")
        error_verificacion_string = True
    #    continue
    elif isinstance(normalizar_string(texto), str):
        error_verificacion_string = False
    #    break
    else:
        print ("error de ingreso. ingrese un nombre")
        error_verificacion_string = True
    #    break
    return texto, salir, error_verificacion_string

def control_ingreso_string_reduced (texto) -> tuple[str, bool, bool]:
    salir : bool = False
    if texto.strip().lower() == "exit":
        salir = True
   #     break
    elif texto.strip() == "":
        print("Ingreso no válido, no se permiten entradas vacías. ingrese nuevamente.")
        error_verificacion_string = True
    #    continue
    elif not texto.find(".") == -1 and texto.replace(".","").isdigit():
        print("Ingreso no válido, ingresó un número decimal. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif not texto.find(",") == -1 and texto.replace(",","").isdigit():
        print("Ingreso no válido, ingresó un número separado por comas. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif texto.isdigit():
        print(".Ingresó un número entero. ingrese nuevamente")
        error_verificacion_string = True
    #    continue
    elif isinstance(normalizar_string(texto), str):
        error_verificacion_string = False
    #    break
    else:
        print ("error de ingreso. ingrese un nombre")
        error_verificacion_string = True
    #    break
    return texto, salir, error_verificacion_string

def validar_numero_random (numero_ticket_generado : int ) -> bool:
    coincide_random : bool = False
    for ticket in tickets:
        if numero_ticket_generado == ticket["numero_ticket"]:
            coincide_random = True
    return coincide_random

""" inicializo variables"""
tickets : list = []
# print(type(tickets))
ticket : dict[str:str, str:str, str:str, str:str]= {}
# print(type(ticket))

numeros_random : tuple = (int, int)
numeros_random = (1000, 9999)

caracteres_especiales : tuple = ()
caracteres_especiales = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?")

ticket = {
            "numero_ticket":"999",
            "nombre":"prueba",
            "sector":"grip",
            "asunto":"BGP unreachable",
            "problema":"la sesion BGP con le peer 209.217.24.13 se encuntra unreachable",
         }

"""
for clave, valor in ticket.items():
    print(f"imprimo clave : valor {clave}:{valor}")
"""

tickets.append(ticket)
# print(tickets)

error_verificacion_string : bool = False

salir = False
while not salir:
    print("Ingrese un ticket siguiendo los proximos 4 pasos. Exit para salir")
 
    while error_verificacion_string == False and salir == False:
        nombre_ingresado = input("ingrese el nombre de la persona que genera el ticket :")
        # print(f"el nombre ingresado es :{nombre_ingresado}")
        nombre_ingresado_validado, salir, error_verificacion_string = control_ingreso_string (nombre_ingresado)
        
        nombre_ingresado_validado = nombre_ingresado_validado.strip()
        nombre_ingresado_validado = nombre_ingresado_validado.lower()
        nombre_ingresado_validado = nombre_ingresado_validado.capitalize()
        
        if error_verificacion_string == True:
            error_verificacion_string = False
            continue
        if salir == True:
            break
        break
    # print(type(nombre_ingresado_validado))
    # print(f"el nombre ingresado es : {nombre_ingresado_validado}")

    while error_verificacion_string == False and salir == False:
        sector_ingresado = input("ingrese el sector de la persona que genera el ticket :")
        # print(f"el sector ingresado es :{sector_ingresado}")
        sector_ingresado_validado, salir, error_verificacion_string = control_ingreso_string (sector_ingresado)
        if error_verificacion_string == True:
            error_verificacion_string = False
            continue
        if salir == True:
            break
        break
    # print(type(sector_ingresado_validado))
    # print(f"el sector ingresado es : {sector_ingresado_validado}")


    while error_verificacion_string == False and salir == False:
        asunto_ingresado = input("ingrese el asunto del ticket :")
        # print (f"el asunto ingresado es :{asunto_ingresado}")
        asunto_ingresado_validado, salir, error_verificacion_string = control_ingreso_string_reduced (asunto_ingresado)
        if error_verificacion_string == True:
            error_verificacion_string = False
            continue
        if salir == True:
            break
        break
    # print(type(asunto_ingresado_validado))
    # print(f"el asunto ingresado es : {asunto_ingresado_validado}")


    while error_verificacion_string == False and salir == False:
        problema_ingresado = input("ingrese el problema que genera el ticket :")
        # print (f"el problema ingresado es :{problema_ingresado}")
        problema_ingresado_validado, salir, error_verificacion_string = control_ingreso_string_reduced (problema_ingresado)
        if problema_ingresado_validado == True:
            error_verificacion_string = False
            continue
        if salir == True:
            break
        break
    # print(type(problema_ingresado_validado))
    # print(f"el problema ingresado es : {problema_ingresado_validado}")
    
    if salir == True:
        continue

    coincide_random = True
    while coincide_random == True:
        numero_ticket_generado : int = randint(numeros_random[0], numeros_random[1])
        coincide_random = validar_numero_random(numero_ticket_generado)
    
    numero_ticket_validado = numero_ticket_generado

    ticket = {  
                "numero_ticket" : numero_ticket_validado, 
                "nombre" : nombre_ingresado_validado,
                "sector" : sector_ingresado_validado,
                "asunto" : asunto_ingresado_validado,
                "problema" : problema_ingresado_validado,
             }
    tickets.append(ticket)
print (tickets)
print ("fin del programa")
