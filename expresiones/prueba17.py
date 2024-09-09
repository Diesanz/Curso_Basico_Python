import re

correos = open("mbox.txt")
contador = 0
suma = 0
expresion= ('^New .*: ([0-9.]+)')

for linea in correos:
    linea = linea.rstrip()
    x = re.findall(expresion,linea)
    if len(x) > 0:
        contador +=1 
        suma = suma +  int(x[0])

promedio = suma/contador

print(f"mbox.txt tiene {contador} líneas que coinciden con {expresion} y a mayores esta expresión busca dígitos y su suma es {suma} y el promedio de la suma es {promedio}")