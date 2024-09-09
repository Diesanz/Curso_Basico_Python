response = input("Quieres leer o escribir (r/w): ")
archivo = input("Dime el archivo: ")

try:
    if response.lower() == "r":
        manejador_archivo = open(archivo)
    elif response.lower() == "w":
        manejador_archivo = open(archivo, 'w')
    else:
        print("Opción no válida")
        exit()
except FileNotFoundError:
    print("Archivo no encontrado")
    exit()
except Exception as e:
    print(f"Error al abrir el archivo: {e}")
    exit()

if response.lower() == "r":
    cont = 0
    for lin in manejador_archivo:
        cont += 1
        lin = lin.rstrip()
        if not lin.startswith("From"):
            continue
        if lin.find('@uct.ac.za') == -1:
            continue
        print(lin)
    manejador_archivo.close()
    print(f"contador: {cont}")
elif response.lower() == "w":
    manejador_archivo.write("Hola Mundo")
    manejador_archivo.close()
