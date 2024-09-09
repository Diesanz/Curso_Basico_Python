import socket

def get_url_input():
    url = input("Introduce una url: ")
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Error: La URL debe comenzar con 'http://' o 'https://'")
        return None
    return url

def main():
    url = get_url_input()
    if not url:
        return

    try:
        urlSplit = url.split('/')
        if len(urlSplit) < 3:
            raise ValueError("URL mal formada.")

        host = urlSplit[2]
        path = '/' + '/'.join(urlSplit[3:]) if len(urlSplit) > 3 else '/'
        
        misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        misock.connect((host, 80))
        llamada = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
        cmd = llamada.encode()
        misock.send(cmd)

        while True:
            datos = misock.recv(512)
            if len(datos) < 1:
                break
            print(datos.decode(), end='')

        misock.close()

    except socket.gaierror:
        print("Error: Host no encontrado.")
    except socket.error as e:
        print(f"Error de conexión: {e}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
