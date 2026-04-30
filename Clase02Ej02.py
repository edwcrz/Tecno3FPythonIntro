try:
    numero = int(input("Ingresá un número: "))
    print("Número válido:", numero)
    if numero > 5:
        print("El número es mayor que 5")
    elif numero == 5:
        print("El número es igual a 5")
    else:
        print("El número es menor que 5")
except ValueError:
    print("Error: no ingresaste un entero")
usuario = str(input("Ingrese el nombre: "))
print ("el usuario ", usuario, "ingreso el numero: ", numero )
usuario = usuario.upper()
print (usuario)
print (f"el usuario ingresado es {usuario} y el numero ingresado es {numero}")
print ("el usuario ingresado es {} y el numero ingresado es {}".format(usuario, numero))
print ("el usuario ingresado es {0} y el numero ingresado es {1}".format(usuario, numero))
print ("el usuario ingresado es {nombre} y el numero ingresado es {numero}".format(nombre=usuario, numero=numero))