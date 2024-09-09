
numeros = list()
contador = 0

while(True):
    numero = input("Dame un numero: ")
    if str(numero) == 'fin':
        break
    try:
        numeros.append(int(numero))
    except:
        print("Esa entrada no es valida ")

print(f"Máximo {max(numeros)}")
print(f"Mínimo {min(numeros)}")