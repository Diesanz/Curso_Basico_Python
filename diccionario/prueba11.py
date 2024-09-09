# Abrir el archivo words.txt en modo lectura
try:
    with open('words.txt', 'r') as archivo:
        # Leer todo el contenido del archivo
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo 'words.txt' no se encontró.")
    exit()
except Exception as e:
    print(f"Error al abrir el archivo: {e}")
    exit()

# Crear un diccionario para almacenar las palabras
diccionario_palabras = {}

# Dividir el contenido en palabras
palabras = contenido.split()

# Almacenar cada palabra como una clave en el diccionario
for palabra in palabras:
    diccionario_palabras[palabra] = None

# Imprimir el diccionario para verificar el resultado
print(diccionario_palabras)
