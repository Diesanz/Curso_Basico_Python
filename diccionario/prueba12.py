correos = open("mbox-short.txt")
listadias = dict()

for correo in correos:
    correo = correo.rstrip()
    if correo.startswith("From"):
        elementos_correo = correo.split()
        if len(elementos_correo) > 2 :
            listadias[elementos_correo[2]] = listadias.get(elementos_correo[2],0)+1
        
print(listadias)