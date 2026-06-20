# hay diferentes tipos de archivos
# .csv .txt .json .yaml .pck
# .txt para guardar frases
# para clave valor un json o csv
# flujo de trabajo con archivos : abrir usar y cerrar el archivo
# sino se puede corromper el archivo
# codificacion legible UTF-8
# codificacion binaria no legible
# el archivo debe estar en el raiz del main
# para read debo primero crar un archivo
# write sobre escribe
# write si no tiene archivo lo crea
# el append crea el archivo si no esta, como write
# si existia, agrega al final

archivord = open('archivord.txt', 'r',encoding='UTF-8')
contenido = archivord.read()
print (f"el contenido del archivo es {contenido}")
print (f"para imprimir hola : {contenido[0:4]}")
archivord.close()

archivowr = open('archivowr.txt', 'w',encoding='UTF-8')
archivowr.write("hola que tal")
archivowr.close()

archivoapnd = open('archivoapnd.txt', 'a',encoding='UTF-8')
archivoapnd.write("\n agrego abajo \n")
archivoapnd.close()

archivord = open('archivoapnd.txt', 'r',encoding='UTF-8')
contenido = archivord.read()
print (contenido)
archivord.close()
