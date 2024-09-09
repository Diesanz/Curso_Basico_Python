
contador = 0
media = 0.0
suma = 0
while True:
    numero = input("Mete un número: ")
    try:
        if numero == "fin":
            media = suma/contador
            break
            
        numero = int(numero)
        suma = suma+numero
        contador = contador+1
    except:
        print("Número no valido")

print("Suma:",suma,"Cont",contador,"Media",media)