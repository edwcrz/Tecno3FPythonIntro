## Realizar un programa que muestre cualquier frase ingresada por el usuario en minuscula
print("Ingrese una frase para mostrarla en minuscula:")
try:
    frase = str(input("Ingrese una frase: "))
    fraseenminuscula = frase.lower()
    print("La frase ingresada en minuscula es: {fraseenminuscula}".format(fraseenminuscula=fraseenminuscula))
except ValueError:
    print("Error: No se pudo convertir la entrada a una cadena.")