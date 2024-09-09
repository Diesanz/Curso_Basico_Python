correos = open("mbox-short.txt")
listadias = dict()
keysList = list()
valuesList = list()

for correo in correos:
    correo = correo.rstrip()
    if correo.startswith("From"):
        elementos_correo = correo.split()
        if len(elementos_correo) > 2 :
            listadias[elementos_correo[1]] = listadias.get(elementos_correo[1],0)+1
        
keysList = list(listadias.keys())
valuesList = list(listadias.values())
maximoCorreos = max(valuesList)
indiceCorreo = valuesList.index(maximoCorreos)
print(keysList[indiceCorreo],maximoCorreos)