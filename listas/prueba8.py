
def recortar (lista):
    lista.pop(0)
    lista.pop(len(lista)-1)

def medio (lista):
    lista2 = lista[1:len(lista)-1]
    return lista2

lista = ['1','2','3','4','5','6']
recortar(lista)
lista2 = medio(lista)
print(lista)
print(lista2)
print(lista)