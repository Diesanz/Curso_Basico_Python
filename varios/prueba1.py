ent = input("Introduzca temperatura: ")
try:
    fahr = float(ent)
    cel = (fahr-32.0)*5.0/9.0
    print(cel)
except:
    print("Eso no es un número")