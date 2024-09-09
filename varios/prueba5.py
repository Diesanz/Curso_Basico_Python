def cuenta_palabras(palabra):
    contador = 0
    for p in palabra:
        contador = contador +1
    return contador

def cuenta_letras(palabra,letra):
    palabra = palabra.lower()
    letra = letra.lower()
    contador = 0
    while len(palabra)> 0:
        indice = palabra.find(letra)
        if  indice == -1:
            break
        palabra = palabra[indice+1:]
        contador = contador +1
    return contador

def cuenta_letras2(palabra, letra):
    palabra = palabra.lower()
    letra = letra.lower()
    contador = 0
    for char in palabra:
        if char == letra:
            contador += 1
    return contador

print(cuenta_letras("banana","a"))
