import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# =============================================================================
# PRÁCTICA 4 - EJERCICIO 1: MODELO EXPONENCIAL DE POBLACIÓN
# Consigna: x'(t) = (a - b) * x(t), con x(0) = 100 en t ∈ [0, 1]
#   i)  a = 10, b = 5  -> a - b = 5  (Crecimiento exponencial)
#  ii)  a = 5,  b = 10 -> a - b = -5 (Extinción / Decrecimiento exponencial)
# iii)  a = 10, b = 10 -> a - b = 0  (Población constante)
# =============================================================================

def modexp(tspan, x0, a, b):
    """
    Función equivalente a 'modexp' de MATLAB.
    Resuelve x'(t) = (a - b) * x(t) usando solve_ivp con método 'RK23' (equivalente a ode23).
    """
    f = lambda t, x: (a - b) * x
    sol = solve_ivp(f, tspan, [x0], method='RK23', rtol=1e-6, atol=1e-8)
    return sol.t, sol.y[0]

# --- SCRIPT PRINCIPAL ---

# Parámetros del problema
x0 = 100           # Población inicial x(0) = 100
tspan = (0, 1)     # Intervalo de tiempo t ∈ [0, 1]

# Valores de las tasas de natalidad (a) y mortalidad (b)
a = [10, 5, 10]
b = [5, 10, 10]

# Crear figura (equivalente a figure(1) y hold on en MATLAB)
plt.figure(figsize=(8, 6))

X_list = []

for i in range(len(a)):
    c = a[i] - b[i]
    t, x = modexp(tspan, x0, a[i], b[i])
    X_list.append(x)
    
    # Graficar cada curva con el mismo formato que en la imagen de MATLAB
    plt.plot(t, x, linewidth=2, label=f'a - b = {c}')

# Personalización exacta del gráfico
plt.title("Solución de x'(t) = (a - b)x(t) con ode23 (RK23 en Python)")
plt.xlabel("Tiempo t")
plt.ylabel("Población x(t)")
plt.ylim([0, 200])
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper right')

# Guardar la imagen para previsualización
plt.savefig("Guías Prácticas/Guía_04/G4_1_plot.png", dpi=150)
plt.show()
