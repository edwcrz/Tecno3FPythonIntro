# from Clase13TPFinalTicketsStringsEC02 import controlar_caracteres_especiales
# from Clase13TPFinalTicketsStringsEC02 import normalizar_string
from Clase13TPFinalTicketsStringsEC02 import control_ingreso_string
from Clase13TPFinalTicketsStringsEC02 import control_ingreso_string_reduced

from Clase13TPFinalTicketsPantallasEC02 import pantalla_limpiar

from Clase13TPFinalTicketsRandomEC02 import validar_numero_random

"""Declaracion de numero random"""
numeros_random : tuple = (int, int)
numeros_random = (1000, 9999)
from random import randint

def ingresar_ticket_default(tickets: list) -> list:
    ticket : dict = {
                    "numero_ticket" : "999",
                    "nombre" : "prueba",
                    "sector" : "grip",
                    "asunto" : "BGP unreachable",
                    "problema" : "la sesion BGP con le peer 209.217.24.13 se encuntra unreachable",
                        }
#   for clave, valor in ticket.items():
#       print(f"imprimo clave : valor {clave}:{valor}")

    tickets.append(ticket)
#   print(tickets)
    return tickets

""" Funcion para ingresar Ticket"""
def ingresar_ticket (tickets : list) -> list:

    error_verificacion_string = False
    salir = False
    pantalla_limpiar()

    while salir == False: 

        while error_verificacion_string == False and salir == False:
        
            nombre_ingresado = input("ingrese su Nombre (Exit para salir):")
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
            sector_ingresado = input("ingrese su Sector (Exit para salir):")
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
            asunto_ingresado = input("ingrese el Asunto (Exit para salir):")
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
            problema_ingresado = input("ingrese la descripcion del problema (Exit para salir):")
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
            coincide_random = validar_numero_random(numero_ticket_generado, tickets)
    
        numero_ticket_validado = numero_ticket_generado

        ticket = {  
                    "numero_ticket" : numero_ticket_validado, 
                    "nombre" : nombre_ingresado_validado,
                    "sector" : sector_ingresado_validado,
                    "asunto" : asunto_ingresado_validado,
                    "problema" : problema_ingresado_validado,
                 }
        tickets.append(ticket)
        salir = True
    return tickets