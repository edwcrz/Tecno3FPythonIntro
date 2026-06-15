texto : str = "holacomoestas"
print(type(texto))
binario  = texto.find(".")
print (f"texto.find(.) devuelve :{binario}")
print(type(binario))
if texto.find(".") == 1:
    print("encontrado")
else:
    print("no encontrado")