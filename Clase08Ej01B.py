## prueba de rotación de caracteres de un string
## pruebo la funcion deque de la libreria collections para rotar los caracteres de un string
from collections import deque
def rotar_string(s, n):
    d = deque(s)
    d.rotate(n)
    return ''.join(d)

print(int(rotar_string("1234", 1))) # rotar a la derecha
print(int(rotar_string("1234", -1))) # rotar a la izquierda
print(int(rotar_string("1234", 2))) # rotar a la derecha dos veces
print(int(rotar_string("1234", -2))) # rotar a la izquierda dos veces
print(int(rotar_string("1234", 0))) # no rotar

string_original = "1234"
caracter_del_string = string_original[0]
print (f"el caracter del string es: {caracter_del_string}")