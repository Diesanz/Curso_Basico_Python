numberOne = 1
numberTwo = 2
numberTwo = "2"

# try except
try:
    print(numberOne + numberTwo)
except:
    print("No se cumplió")

# try except else finally
try:
    print(numberOne + numberTwo)
except:
    print("Error")
else:
    # Se ejecuta si no se produce excepción
    print("La ejecución continúa correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecución continúa")

# except type
try:
    print(numberOne + numberTwo)
except TypeError as t:
    print("TypeError:", t)

# except value
try:
    print(numberOne + numberTwo)
except ValueError as e:
    print("ValueError:", e)

# Capturar la información
try:
    print(numberOne + numberTwo)
except ValueError as e:
    print("ValueError:", e)
except TypeError as t:
    print("TypeError:", t)
