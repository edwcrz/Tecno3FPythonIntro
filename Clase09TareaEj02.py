## Cree una funcion que determine si un color es primario o no,
## se debe imprimir por pantalla la leyenda “el color X es primario“ 
## o “el color X no es primario”
def es_color_primario(color: str) -> bool:
    colores_primarios = ["rojo", "amarillo", "azul"]
    colores_secundarios = ["naranja", "verde", "violeta"]
    colores_terciarios = ["marron", "rosa", "gris", "blanco", "negro"]
    if color.lower() in colores_secundarios:
        return False
    if color.lower() in colores_terciarios:
        return False
    return color.lower() in colores_primarios

# Ejemplo de uso
color = input("Ingrese un color: ")
if es_color_primario(color):  
    print(f"el color {color} es primario")
else:
    print(f"el color {color} no es primario")
