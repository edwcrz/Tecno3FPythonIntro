## practica de tipos de datos y estructuras de datos
## ingreso paises a una lista de paises
## no ingresar numeros enteros, numeros decimales con coma, caracteres especiales, ni espacios vacios

# tuplas
caracteres_especiales : tuple = ()
# print (type(caracteres_especiales))


caracteres_especiales = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?")
# print(type(caracteres_especiales))
# print(caracteres_especiales)

# for i in range(len(caracteres_especiales)):
#     print(caracteres_especiales[i])

# for caracter_especial in caracteres_especiales:
#    print(caracter_especial)


# funcion controlar que no haya caracteres especiales en un strint
def controlar_caracteres_especiales(texto: list, caracteres_especiales: tuple) -> bool:
    for caracter in texto:
        for car in caracteres_especiales:
            if caracter == car:
                return True
                break






# listas

def convertir_numero(texto):
    try:
        return int(texto)
    except ValueError:
        try:
            return float(texto)
        except ValueError:
            return str(texto)


paises = list()
# print(type(paises))

# paises: list[str] = []

# print(type(paises))
paises_america_latina = ["Argentina", "Brasil", "Chile", "Colombia", "Ecuador", "Peru", "Uruguay", "Venezuela"]
cantidad_paises_latam = len(paises_america_latina)
# print(f"Cantidad de países en América Latina: {cantidad_paises_latam}") 
# print (paises_america_latina)

paises_america_central = ["Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panama"]
cantidad_paises_america_central = len(paises_america_central)
# print(f"Cantidad de países en América Latina: {cantidad_paises_america_central}") 
# print (paises_america_central)

paises_america_norte = ["Canada", "Estados Unidos", "Mexico"]
cantidad_paises_america_norte = len(paises_america_norte)
# print(f"Cantidad de países en América Latina: {cantidad_paises_america_norte}") 
# print (paises_america_norte)

paises_europa = ["Alemania", "Francia", "Italia", "España", "Reino Unido"]
cantidad_paises_europa = len(paises_europa)
# print(f"Cantidad de países en América Latina: {cantidad_paises_europa}") 
# print (paises_europa)

paises_asia = ["China", "India", "Japón", "Corea del Sur", "Indonesia"]
cantidad_paises_asia = len(paises_asia)
# print(f"Cantidad de países en América Latina: {cantidad_paises_asia}") 
# print (paises_asia)

paises_africa = ["Nigeria", "Egipto", "Sudáfrica", "Etiopía", "Kenya"]
cantidad_paises_africa = len(paises_africa)
# print(f"Cantidad de países en América Latina: {cantidad_paises_africa}") 
# print (paises_africa)

paises_oceania = ["Australia", "Nueva Zelanda", "Fiyi", "Papúa Nueva Guinea", "Samoa"]
cantidad_paises_oceania = len(paises_oceania)
# print(f"Cantidad de países en América Latina: {cantidad_paises_oceania}") 
#   print (paises_oceania)

paises.extend(paises_america_latina)
paises.extend(paises_america_central)
paises.extend(paises_america_norte)
paises.extend(paises_europa)
paises.extend(paises_asia)
paises.extend(paises_africa)
paises.extend(paises_oceania)

paises.sort()   

# print(type(paises)) 

# print(paises[0])
# print(paises[1])
# print(paises[2])
# print(paises[3])
# print(paises[4])
# print(paises[5])
# print(paises[6])
# print(paises[7])
# print(paises[8])
# print(paises[9])
# print(paises[-1])
# print(paises[-2])

# for i in range(len(paises)):
#    print(paises[i])

# for pais in paises:
#     print(pais)

# condicion = isinstance(paises, list)
# print(condicion)
# condicion = isinstance(paises[0], str)
# print(condicion)

      
# if condicion == True:
#    print(f"El elemento en la posición 0 es una cadena de texto: {paises[0]}")
# else:
#    print(f"El elemento en la posición 0 no es una cadena de texto: {paises[0]}")

i : int = 0

while True:
    pais = input("Ingrese un país (o 'salir' para terminar): ")
    print(f"El país ingresado es: {pais}")
    
    lista_caracteres_pais = list(pais)
    print(f"Lista de caracteres del país ingresado: {lista_caracteres_pais}")
    for i in range(len(lista_caracteres_pais)):
        caracter_lista = lista_caracteres_pais[i]
        print(f"Carácter en la posición {i}: {caracter_lista}")

    pais = pais.strip()  # Eliminar espacios en blanco al inicio y al final
    pais = pais.lower()  # Asegurar que la primera letra del país esté en mayúscula
    pais = pais.capitalize()  # Asegurar que la primera letra del país esté en mayúscula

    if pais.lower() == "salir":
        break
    elif pais in paises:
        print(f"{pais} ya está en la lista.")
    elif not isinstance(convertir_numero(pais), str):
        print("Ingreso no válido. Ingresaste un nùmero. Por favor, ingrese un nombre de país.")
    elif pais.strip() == "":
        print("Ingreso no válido. No se permiten entradas vacías. Por favor, ingrese un nombre de país.")
    elif pais.replace(",", "").isdigit():
        print("Ingreso no válido. Ingresaste un número con coma. Por favor, ingrese un nombre de país.")
    elif controlar_caracteres_especiales(lista_caracteres_pais, caracteres_especiales):
        print("Ingreso no válido. El nombre del país contiene caracteres especiales. Por favor, ingrese un nombre de país válido.")
    else:
        paises.append(pais)
        print(f"{pais} ha sido agregado a la lista.")
print("Lista final de países:", paises)
