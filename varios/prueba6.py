str = 'X-DSPAN-Confidence:0.8475'
posicion_extraer = str.find(':')
texto_extraido = str[posicion_extraer+1:]
print(float(texto_extraido))