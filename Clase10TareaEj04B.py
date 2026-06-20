"""Vamos a crear un programa en python donde 
   vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
   El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y 
   nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario."""

""" Bienvenida"""

""" Adicional recibo los ticket de peso en un diccionario"""

print ("Bienvenido al ejercicio 04 de la tarea de la clase 11")

precios_frutas : dict = {}
# print(type(precios_frutas))
precios_frutas = {
                    "naranja" : 3000,
                    "manzana": 4000,
                    "banana" : 5000,
                    "melon" : 6000,
                    "sandia" : 7000,
                    "kiwi" : 8000,
                 }
print (f"los precios de la fruta a la venta son: {precios_frutas}")

# print(f"Elija las cantidades que necesite de las siguientes frutas disponibles: {precios_frutas.keys()}")
# print(f"los precios por kilo correspondientes a la lista de frutas disponible son : {precios_frutas.values()}")

# for clave, valor in precios_frutas.items():
#    print (clave, ":",  valor)

precio : float = 0
peso : int = 0

def calcular_consumo (fruta: str, peso: int) -> float:
    for clave_fruta, key_valor in precios_frutas.items():
        if clave_fruta == fruta:
            precio = float(key_valor * peso)
            return precio

while True:
    fruta = str(input("ingrese una fruta de la lista de frutas disponibles. ingrese Exit para salir :"))
    print (fruta)
    if fruta == "Exit":
        break
    peso = int(input("ingrese el peso de la fruta. Ingrese Exit para salir :"))
    print (peso)
    if peso == "Exit":
        break
    precio = calcular_consumo(fruta, peso)
##    for clave_fruta, key_valor in precios_frutas.items():
##        if clave_fruta == fruta:
##            precio = key_valor * peso
    print(f"El precio de la fruta {fruta} por {peso} kg que lleva es: {precio}")