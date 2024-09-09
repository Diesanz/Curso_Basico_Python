
horasTrabajadas = input("Horas trabajadas:\n")
tarifaHora = input("Tarifa por hora:\n")

diferenciaHoras = 0

def calculoSalario(horasTrabajadas,tarifaHora):
    
    if horasTrabajadas > 40:
        diferenciaHoras = horasTrabajadas - 40
        salarioNormal = 40 * tarifaHora
        salarioExtra = diferenciaHoras * 1.5 * tarifaHora
    else:
        salarioNormal = horasTrabajadas * tarifaHora
        salarioExtra = 0
    
    salarioFinal = salarioNormal + salarioExtra
    return salarioFinal

try:

    horasTrabajadas = int(horasTrabajadas)
    tarifaHora = int(tarifaHora)
    salarioFinal = calculoSalario(horasTrabajadas,tarifaHora)

    print(f"Salario final: {salarioFinal}")

except ValueError:
    print("Los valores ingresados no son válidos. Por favor ingresa números enteros.")
