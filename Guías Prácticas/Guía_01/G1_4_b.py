# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:50:00 2026

@author: ribni
"""


"""
CONSIGNA 4. B
Para el sistema:

    • Discretizar los siguientes sistemas de ecuaciones diferenciales para t ∈ [0, 5] 
      usando el algoritmo de Euler con paso h.
    • Escribir un código para resolver numéricamente el sistema discretizado.
    • Simular el sistema con paso h = 0.5 seg., h = 0.1 seg., h = 0.05 seg. para 
      aproximar la solución del sistema de ecuaciones diferenciales en el t0 dado.
    • Hacer un cuadro con los resultados obtenidos para los distintos valores h.

(b) dx/dt = y,  dy/dt = x - y
    x(0) = 1, y(0) = 2, t0 = 1
"""

#%% LIBRERÍAS
import numpy as np
# import matplotlib.pyplot as plt
# import math

#%% PARÁMETROS
# Condiciones iniciales --> se agrupan en un vector
# Nuestro "estado inicial" que tiene a x0 (1.0) e y0 (2.0)
estado_inicial = np.array([1.0, 2.0]) 
t0 = 0

# Condiciones finales (queremos evaluar en t=2)
tf = 1

# pasos
pasos_h = [0.5, 0.1, 0.05]

#%% FUNCIONES

# Método de discretización de Euler:
# Permite predecir el futuro dando saltos de tiempo h (pasos de simulación)

def metodo_euler(f, t0, tf, y0, N):
    """Implementación del Método de Euler (yk+1 = yk + h * f(tk, yk))"""
    h = (tf - t0) / N # Calcula el tamaño del paso h --> Cuanto tiempo avanza en cada iteraciom
    # Si haces mas pasos N, el I (t0, tf) se divide en porciones mas chicas --> mayor precision
    t, y = t0, y0
    for _ in range(N):
        # FORMULA de EULER --> f(t,y) es la derivada, la pendiente en un punto, y si se multiplica por h te da cuanto cambia y
        y = y + h * f(t, y)
        t = t + h # actualizas el tiempo
    return y #--> aproximacion de y(tf)

# Ecuación del ejercicio
def f_edo_b(t, estado):
    # El primer elemento (índice 0) es 'x', el segundo (índice 1) es 'y'
    x = estado[0]
    y = estado[1]
    
    # Ecuaciones
    dx_dt = y
    dy_dt = x - y
    
    # Dev. derivadas en un vector
    return np.array([dx_dt, dy_dt])


#%% SCRIPT

# cuadro comparativo (Ajustamos el encabezado para que entren las 4 columnas de datos alineadas)
print(f"{'Paso (h)':<15}{'Pasos (N)':<15}{'Resultado x(t0)':<20}{'Resultado y(t0)':<20}")


# Iteramos sobre cada paso h para calcular el resultado
for h in pasos_h:
    # Calculamos N (usamos round e int para que sea un número entero perfecto)
    N = int(round((tf - t0) / h))
    
    # llamo a la funcion (f_edo, t0, tf, x0, N)
    resultado = metodo_euler(f_edo_b, t0, tf, estado_inicial, N)
    
    # Desempaquetamos los resultados finales para poder imprimirlos por separado
    x_final = resultado[0]
    y_final = resultado[1]
    
    # Imprimimos la fila del cuadro (Alineamos los datos con el formato <15 del encabezado)
    print(f"{h:<15}{N:<15}{x_final:<20.6f}{y_final:<20.6f}")