import time
from datetime import datetime

# Decorador que mide el tiempo de ejecución de una función
def tiempo_de_ejecucion(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️ Tiempo de ejecución de {func.__name__}: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

# Decorador que registra las acciones en un archivo de log
def registro_de_acciones(func):
    def wrapper(*args, **kwargs):
        with open("acciones.log", "a") as log:
            log.write(f"[{datetime.now()}] Acción ejecutada: {func.__name__} con args: {args}, kwargs: {kwargs}\n")
        return func(*args, **kwargs)
    return wrapper

# Decorador que verifica la autenticación del usuario con un token (simulado)
def requiere_autenticacion(func):
    def wrapper(*args, **kwargs):
        token = input("🔑 Introduce tu token: ")
        if token != "secreto":
            print("Autenticación fallida. Token inválido.")
            return
        print("✅ Autenticación exitosa.")
        return func(*args, **kwargs)
    return wrapper

# Función que simula escanear puertos
@tiempo_de_ejecucion
@registro_de_acciones
def escanear_puertos(ip):
    print(f"Escaneando puertos en {ip}...")
    time.sleep(2)  # Simula el tiempo de escaneo
    print("✅ Escaneo completo.")

# Función que simula lanzar un exploit
@requiere_autenticacion
def lanzar_exploit(ip):
    print(f"Lanzando exploit contra {ip}...")
    time.sleep(3)  # Simula el tiempo de ataque
    print("✅ Exploit ejecutado.")

# Ejemplo de ejecución
escanear_puertos("192.168.1.1")
lanzar_exploit("192.168.1.2")
