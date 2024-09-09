correos = open("mbox-short.txt")
listadias = dict()


for correo in correos:
    correo = correo.rstrip()
    if correo.startswith("From"):
        elementos_correo = correo.split()
        if len(elementos_correo) > 2 :
            listadias[elementos_correo[1]] = listadias.get(elementos_correo[1],0)+1
        
listaTuplas = list()

for clave, valor in listadias.items():
    listaTuplas.append((valor,clave))
listaTuplas.sort(reverse=True)
print(listaTuplas[0])