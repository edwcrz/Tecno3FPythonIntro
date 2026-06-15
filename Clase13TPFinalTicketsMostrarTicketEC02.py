"""Funcion para mostrar los identificadores de los tickets registrados"""
def mostrar_tickets (tickets : list) -> list:
    ticket_list : list = []
    ticket_barre : dict = {}
    for ticket_barre in tickets:
        ticket_list.append(ticket_barre["numero_ticket"])
    # print (f"la lista de tickets es :{ticket_list}")
    return ticket_list
