import string

def cambiar_frase(frase):
    frase = frase.translate(str.maketrans('','',string.punctuation)) #quitar signos puntuación
    frase = frase.lower() #a minusculas todo
    frase = frase.translate(str.maketrans('', '', string.digits))
    frase = ''.join([char for char in frase if char.isalpha()]) #quitar tabulciones y espacios
    return frase

archivo = input("Dime el archivo: ")
diccionario_palabras = dict()

try:
    lectura = open(archivo)
except:
    print("No existe ese archivo ")
    exit()

for frase in lectura:
    frase = cambiar_frase(frase)
    frase.split() #sin espacios
    for palabras in frase:
        diccionario_palabras[palabras] = diccionario_palabras.get(palabras,0)+1
    
lista_palabras = list()

for clave,valor in diccionario_palabras.items():
    lista_palabras.append((valor,clave))

lista_palabras.sort(reverse=True)

print(lista_palabras)