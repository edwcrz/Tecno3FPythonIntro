"""Funcion para leer ticket"""
def leer_ticket (numero_ticket_leer : int, tickets : list) :
    # lista_numero_tickets : list = []
    ticket_barre : dict = {}
    for ticket_barre in tickets:
        if numero_ticket_leer == ticket_barre["numero_ticket"]:
            return ticket_barre