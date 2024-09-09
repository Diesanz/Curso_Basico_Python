import re

correos = open("mbox.txt")
contador = 0

expresion = str(input("Ingrese una expresión regular: "))

if expresion == " ":
    print("Esa expresión no se puede ")
    exit()
else:
    for linea in correos:
        linea = linea.rstrip()
        x = re.findall(expresion,linea)
        if len(x) > 0: contador +=1

print(f"mbox.txt tiene {contador} líneas que coinciden con {expresion}")