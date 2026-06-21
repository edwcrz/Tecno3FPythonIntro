import string
from secrets import choice
import sys

# les paso un diccionario donde cada valor tendra una cadena, es decir letras tiene una cadena del alfabeto en mayusculas y minusculas, numeros tiene la cadena de numeros del 0 al 9 y lo mismo con caracteres

# print (string.digits)
# print (string.ascii_lowercase)
# print (string.ascii_uppercase)
# print (string.punctuation)

def validar_int (numero: int) -> bool:
    if numero.isdigit() == True:
        largo_password_validado = True
    else:
        largo_password_validado = False
    return (largo_password_validado)

dict_permitido  = {
                    'letras_minusculas': string.ascii_lowercase,
                    'letras_mayusculas': string.ascii_uppercase,
                    'numeros': string.digits,
                    'caracteres': string.punctuation
                }


largo_min : int = 12
salir : bool = True
password : str = ""
lista_acumulador : list = []

print ("bienvenido al programa de generación de password")
print ("la password generada tendrá al menos una letra mayúscula, al emnos un caracter especial y al menos un numero")
error_int : bool = True
largo_password_validado = False

while salir == True:
    
    while error_int == True:
        largo_password = input("ingrese la longitud de la password a generar de al menos 12 caracteres : ")
        largo_password_validado = validar_int(largo_password)
        
        if not largo_password_validado:
            continue    
        largo_password = int(largo_password)
                
        if largo_password < largo_min:
            print("ingreso una password de menos de 12 caracteres : ")
            continue
        error_int = False
    salir = False
# print (largo_password)

caracteres_permitidos = dict_permitido['letras_minusculas'] + dict_permitido['letras_mayusculas'] + dict_permitido ['numeros'] + dict_permitido['caracteres']
# print(caracteres_permitidos)

for i in range (largo_password):
    lista_acumulador.append (choice(caracteres_permitidos))
# print (lista_acumulador)

password = "".join(lista_acumulador)
print (password)
