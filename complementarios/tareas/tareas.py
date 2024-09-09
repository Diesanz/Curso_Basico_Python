toDo = list()

# Leer tareas desde el archivo
try:
    with open("tareas.txt", "r") as tareas_archivo:
        for linea in tareas_archivo:
            toDo.append(linea.strip())  # Elimina el salto de línea al leer
except FileNotFoundError:
    print("Archivo no encontrado")
    exit()
except Exception as e:
    print(f"Error al abrir el archivo: {e}")
    exit()

# Función para añadir tareas
def anadir_tarea():
    print("Escribe las tareas, escribe <f> para salir ")
    while True:
        tarea = input()
        if tarea.lower() == 'f':
            break
        else:
            toDo.append(tarea)

# Función para mostrar tareas
def mostrar_tarea():
    for i, tarea in enumerate(toDo):
        print(f"{i}. {tarea}")

def marcar_tarea():
    print("Ecribe tareas a marcar, escribe <f> para salir ")
    while True:
        tarea = input()
        if tarea.lower() == 'f':
            break
        else:
            toDo.remove(tarea)

# Función para guardar tareas y salir del programa
def salir():
    print("Saliendo del programa ")
    with open("tareas.txt", "w") as anadir_tareas_archivo:
        for to in toDo:
            anadir_tareas_archivo.write(to + '\n')

# Función principal del programa
def main():
    while True:
        try:
            print("1. Añadir Tarea")
            print("2. Mostrar Tareas Pendientes")
            print("3. Marcar Tareas Pendientes")
            print("4. Volver")
            opt = int(input("Qué deseas hacer: "))
        except ValueError:
            print("Opción no válida")
            continue

        if opt == 1:
            anadir_tarea()
        elif opt == 2:
            mostrar_tarea()
        elif opt == 3:
            marcar_tarea()  
        elif opt == 4:
            salir()
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
