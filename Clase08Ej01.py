## Titulo: Descubra el PIN
## requerimiento
## El juego termina cuando 
## A - el usuario acierta la clave o 
## B - hace 3 intentos.
## Al pedir el ingreso, 
## se debe validar que el dato tenga 
## A - exactamente 4 caracteres y 
## B - que sean únicamente dígitos numéricos enteros. 
## Si no cumple, no consume intento y vuelve a pedirlo.
## Si el usuario falla, el sistema debe indicar: 
## cuántos números de su intento son correctos y
## cuántos de ellos están en la posición correcta.
## Al perder (agotar los intentos), 
## se le enviará un mensaje indicándole que el sistema fue bloqueado y 
## cuál era la clave correcta.

## Desarrollo
## 010 definir cantidad de intentos en 3
## 020 generar un pin de 4 digitos random
## 030 mientras el intento sea menor a la cantidad de intentos permitidos:
## 040 pedir al usuario que ingrese un pin
## 050 validar que tenga 4 caraceteres
## 060 validar que sean dígitos numéricos enteros
## 070 si no cumple el ingreso no consumir intento y volver a pedir el ingreso
## 080 comparar el ingreso con el pin generado
## 090 contar el intento
## 100 contar intentos faltantes
## 110 si el ingreso es igual al pin generado, mostrar mensaje de éxito y terminar el juego
## 120 si el ingreso no es igual al pin generado:
## 130 contar cuántos números son correctos e informar al usuario
## 140 contar cuántos están en la posición correcta e informar al usuario
## 150 si se agotaron los intentos, mostrar mensaje de bloqueo y revelar el pin correcto

print ("¡Bienvenido al programa en python para descubrir el PIN de 4 dígitos!")
from random import randint
from collections import deque

# defino la función para rotar el pin
def rotar_pin(pin, n):
    d = deque(pin)
    d.rotate(n)
    return ''.join(d)

# definir cantidad de intentos
intentos_permitidos = 5
print (f"la cantidad de intentos permitidos es: {intentos_permitidos}")
# defino la longitud del pin
longitud_pin = 4
print (f"la longitud del pin es: {longitud_pin} dígitos")
# genero y asigno el pin
pin_correcto = f"{randint(0000, 9999):04d}"
## print (f"El pin correcto es: {pin_correcto}")
intentos = 0
posicion = 0

salir = False
while intentos < intentos_permitidos and not salir:
    contador_se_encuentra = 0
    contador_posicion_correcta = 0
    pin_ingresado = input("Ingrese un PIN de 4 dígitos: ")
    if not (len(pin_ingresado) == longitud_pin and pin_ingresado.isdigit()):
        print ("Ingreso inválido. Asegúrese de ingresar exactamente 4 dígitos numéricos.")
        continue
    intentos += 1
    intentos_restantes = intentos_permitidos - intentos
    se_encuentra = False
    posicion_correcta = False
    if pin_ingresado == pin_correcto:
        print (f"Excelente ingresaste el PIN correcto: {pin_correcto}")
        salir = True
    else:
        print (f"Ingresaste un PIN incorrecto. Te quedan {intentos_restantes} intentos.")
        for posicion in range (longitud_pin):
            pin_rotado = rotar_pin(pin_correcto, -posicion)
            # print (f"El pin rotado en {posicion} posiciones es: {pin_rotado}")
            if pin_ingresado[posicion] == pin_rotado[0]:
                print (f"El número {pin_ingresado[posicion]} está en la posición correcta.")
                contador_posicion_correcta += 1
            else:
                j = 0
                posicion_barrido = posicion
                for j in range (longitud_pin-1):
                    posicion_barrido = posicion_barrido+1
                    pin_barrido = rotar_pin(pin_correcto, -posicion_barrido)
                    # print (f"El pin rotado en {posicion_barrido} posiciones es: {pin_barrido}")
                    if pin_ingresado[posicion] == pin_barrido[0]:
                       se_encuentra = True
                       contador_se_encuentra += 1
                    else:
                       se_encuentra = False
                   
        print (f"se encontraron {contador_se_encuentra} números en otra posción del PIN.")
        print (f"se encontraron {contador_posicion_correcta} números en la posición correcta.")
print (f"PIN Bloqueado. Se agotaron los {intentos_permitidos} intentos.")
print (f"El pin correcto es: {pin_correcto}")
