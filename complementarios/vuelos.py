vuelos = [("V1", 10), ("V2", 10), ("V3", 10), ("V4", 10)]
vuelos_usuarios = list()
usuarios = list()

def registrarse():
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    if nombre_usuario not in usuarios:
        usuarios.append(nombre_usuario)
        print("Usuario registrado")
    else:
        print("Nombre no disponible")

def reservar(nombre_usuario):
    if nombre_usuario not in usuarios:
        print("Usuario no registrado")
    else:
        while True:
            try:
                numero_vuelo = int(input("Número de vuelo: ")) - 1  # Ajuste para índice de lista
                if numero_vuelo < 0 or numero_vuelo >= len(vuelos):
                    print("Número de vuelo no válido, intente de nuevo.")
                    continue
                
                vuelo = vuelos[numero_vuelo]
                espacio = int(vuelo[1])
                
                if espacio <= 0:
                    print("Vuelo completo, seleccione otro")
                else:
                    vuelos[numero_vuelo] = (vuelo[0], espacio - 1)
                    vuelos_usuarios.append((nombre_usuario, numero_vuelo))
                    print("Reservado\n")
                    break
            except ValueError:
                print("Entrada no válida, por favor ingrese un número de vuelo válido.")

def anular(nombre_usuario, vuelo_usuario):
    if nombre_usuario not in usuarios or vuelo_usuario < 1 or vuelo_usuario > 4:
        print("Revise los datos introducidos")
    else:
        vuelo_usuario -= 1  # Ajuste para índice de lista
        if (nombre_usuario, vuelo_usuario) not in vuelos_usuarios:
            print("Reserva no encontrada")
        else:
            vuelos_usuarios.remove((nombre_usuario, vuelo_usuario))
            vuelo = vuelos[vuelo_usuario]
            vuelos[vuelo_usuario] = (vuelo[0], vuelo[1] + 1)
            print("Vuelo eliminado")

def menu():
    while True:
        try:
            print("\n***************************")
            print("*****Reserva de Vuelos*****")
            print("***************************\n")
            print("Elige una opción:")
            print("1. Registrarse")
            print("2. Reservar")
            print("3. Anular")
            print("1234. Salir\n")

            option = int(input("Selecciona una opción: "))
            if option == 1234:
                print("Saliendo del programa.")
                break
            elif option not in [1, 2, 3]:
                print("Esa opción no está disponible.")
            else:
                if option == 1:
                    registrarse()
                elif option == 2:
                    nombre_usuario = input("Introduce nombre de usuario: ")
                    reservar(nombre_usuario)
                elif option == 3:
                    nombre_usuario = input("Introduce nombre de usuario: ")
                    try:
                        vuelo_usuario = int(input("Introduce el número de vuelo del usuario: "))
                        anular(nombre_usuario, vuelo_usuario)
                    except ValueError:
                        print("Número de vuelo no válido, por favor ingrese un número.")
        except ValueError:
            print("Opción no válida")

# Llamar a la función del menú
menu()
