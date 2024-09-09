import numpy as np
import matplotlib.pyplot as plt

def plot_elipse(a, b):
    # Parámetro t va de 0 a 2*pi
    t = np.linspace(0, 2*np.pi, 100)
    
    # Ecuaciones paramétricas de la elipse
    x = a * np.cos(t)
    y = b * np.sin(t)
    
    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Graficar la elipse
    ax.plot(x, y, label=f'Elipse: a={a}, b={b}')
    
    # Configurar el aspecto del gráfico
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()
    
    # Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # Título del gráfico
    ax.set_title('Elipse')
    
    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
a = 2.0  # Semieje mayor
b = 1.5  # Semieje menor

plot_elipse(a, b)
