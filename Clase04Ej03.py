## Realizar un programa que le pida al usuario su nombre y apellido , Mostrarlos en un mensaje de bienvenida por la pantalla
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
print("Bienvenido/a {nombre} {apellido} !".format(nombre=nombre, apellido=apellido))