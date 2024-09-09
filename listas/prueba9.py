
obra = open("romeo.txt")
obraOrdenada = list()
for romeo in obra:
    julieta = romeo.split()
    for romeoJulieta in julieta:
        if romeoJulieta in list():continue
        obraOrdenada.append(romeoJulieta)
    
obraOrdenada.sort()
print(obraOrdenada)