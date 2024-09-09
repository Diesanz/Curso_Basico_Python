import urllib.request, urllib.parse, urllib.error
import json
import ssl

clave_api = False
#clave_api = 'AIzaSy___IDByT70'

if clave_api is False:
    clave_api = 42
    url_de_servicio = 'http://py4e-data.dr-chuck.net/json?'
else :
    url_de_servicio = 'https://maps.googleapis.com/maps/api/geocode/json?'

#Ignorar errores de certificado SSl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    direccion = input("Ingresa tu ubicacion: ")
    if len(direccion) < 1: break

    parms = dict()
    parms['address'] = direccion
    if clave_api is not False:
        parms['key'] = clave_api
    url = url_de_servicio + urllib.parse.urlencode(parms)

    print("Recuperando", url)
    uh = urllib.request.urlopen(url, context=ctx)
    datos = uh.read().decode()
    print("Recuperados ", len(datos), "caracteres")

    try:
        js = json.loads(datos)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Error al Recuperar ====')
        print(datos)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

    #imprimir el codigo del pais
    components = js['results'][0]['address_components']
    country = None
    for compo in components:
        types = compo['types']
        if 'country' in types:
            country = compo['short_name']
            break
    if country:
        print('Código de país:', country)
    else:
        print('No se encontró el código de país')