"""Vamos a crear un programa en python donde 
   vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
   El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y 
   nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario."""

""" Bienvenida"""

""" Adicional recibo los ticket de peso en un diccionario"""

print ("Bienvenido al ejercicio 04 de la tarea de la clase 11")

frutas_precios : dict = {}
# print(type(precios_frutas))
frutas_precios = {
                    "naranja" : 3000,
                    "manzana": 4000,
                    "banana" : 5000,
                    "melon" : 6000,
                    "sandia" : 7000,
                    "kiwi" : 8000,
                 }
# print (f"los precios de la fruta a la venta son: {frutas_precios}")

# print(f"Elija las cantidades que necesite de las siguientes frutas disponibles: {precios_frutas.keys()}")
# print(f"los precios por kilo correspondientes a la lista de frutas disponible son : {precios_frutas.values()}")

# for clave, valor in precios_frutas.items():
#    print (clave, ":",  valor)

frutas_disponibles = list(frutas_precios.keys())
print (f"las frutas disponibles a la venta son : {frutas_disponibles}")

def verificar_fruta_disponible (fruta: str, frutas_disponibles: list) -> bool:
    disponible: bool = False
    for fruta_barre in frutas_disponibles:
        if fruta == fruta_barre:
            disponible = True
            return disponible

frutas_consumo : dict[str, float] = {}

precio : float = 0

def normalizar_fruta (fruta: str) -> str:
    fruta = fruta.strip()
    fruta = fruta.lower()
    # fruta = fruta.capitalize()
    return fruta

def calcular_consumo (fruta: str, peso: float) -> float:
    for clave_fruta, key_valor in frutas_precios.items():
        if clave_fruta == fruta:
            precio = key_valor * float(peso)
            return precio

caracteres_especiales : tuple = ()
caracteres_especiales = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?")

# funcion controlar que no haya caracteres especiales en un strint
def controlar_caracteres_especiales(fruta: str, caracteres_especiales: tuple) -> bool:
    fruta_list = list()
    fruta_list = list(fruta)
    for caracter in fruta_list:
        for char_especial in caracteres_especiales:
            if caracter == char_especial:
                return True

def convertir_numero(texto):
    try:
        return int(texto)
    except ValueError:
        try:
            return float(texto)
        except ValueError:
            return str(texto)


while True:
    fruta = input("ingrese una fruta de la lista de frutas disponibles. ingrese Exit para salir :")
    print (f"se ingreso :{fruta}")

    if fruta.lower() == "exit":
        break
    elif fruta.strip() == "":
        print("Ingreso no válido. No se permiten entradas vacías. Por favor, ingrese una fruta.")
        continue
    elif not isinstance(convertir_numero(fruta), str):
        print("Ingreso no válido. Ingresaste un nùmero. Por favor, ingrese una fruta.")
        continue
    elif fruta.replace(",", "").isdigit():
        print("Ingreso no válido. Ingresaste un número con coma. Por favor, ingrese una fruta.")
        continue
    elif controlar_caracteres_especiales(fruta, caracteres_especiales):
        print("Ingreso no válido. El nombre de la fruta contiene al menos un caracter especial. Por favor, ingrese una fruta disponible de la lista.")
        continue
    elif not verificar_fruta_disponible(fruta, frutas_disponibles):
        print(f"{fruta} no esta en la lista de frutas disponibles.")
        continue
    else:
        fruta = normalizar_fruta(fruta)
        while True:
            peso = input("ingrese el peso de la fruta. Ingrese Exit para salir :")
            print (f"por la fruta: {fruta} ingreso el siguiente peso: {peso}")
            if peso.lower() == "Exit":
                print (f"ingrese un peso en formato numerico. Si es un decimal ingrese con punto.")
                break
            elif peso.strip() == "":
                print("Ingreso no válido. No se permiten entradas vacías. Por favor, ingrese el peso de la fruta.")
                continue
            elif peso.find(",") != -1 and peso.replace(",","").isdigit():
                print("Ingreso no válido. Ingresaste un número con coma. Por favor, ingrese el peso de la fruta con formato decimal separado por punto.")
                continue
            elif peso.find(".") != -1 and not peso.replace(".","").isdigit():
                print("Ingreso no válido. no ingresaste un número. Por favor, ingrese el peso de la fruta.")
                continue
            else :
                peso = float(peso)
                precio_subtotal = calcular_consumo(fruta, peso)
                # print(f"El precio de la fruta {fruta} por {peso} kg que lleva es: {precio}")
                frutas_consumo.update({fruta : precio_subtotal})
                print (f"el subtotal de los items ingresados es {frutas_consumo}")
                break