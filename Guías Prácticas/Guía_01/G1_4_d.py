# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:14:22 2026

@author: ribni
"""


"""
CONSIGNA 4. D
Para el sistema:

    • Discretizar los siguientes sistemas de ecuaciones diferenciales para t ∈ [0, 5] 
      usando el algoritmo de Euler con paso h.
    • Escribir un código para resolver numéricamente el sistema discretizado.
    • Simular el sistema con paso h = 0.5 seg., h = 0.1 seg., h = 0.05 seg. para 
      aproximar la solución del sistema de ecuaciones diferenciales en el t0 dado.
    • Hacer un cuadro con los resultados obtenidos para los distintos valores h.

(d) dx1/dt = x2,  dx2/dt = x3,  dx3/dt = -2*x1 - 3*x2 - 4*x3
     y = 7*x1 - 5*x2
     x1(0) = 2, x2(0) = 1, x3(0) = 0, t0 = 1
"""

#%% LIBRERÍAS
import numpy as np
# import matplotlib.pyplot as plt
# import math

#%% PARÁMETROS
# Condiciones iniciales --> se agrupan en un vector
# Nuestro "estado inicial" que tiene a x1 (2.0) x2 (1.0) x3 (0.0)
estado_inicial = np.array([2.0, 1.0, 0.0]) 
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
def f_edo_d(t, estado):
    # Desempaquetamos las 3 variables de estado internas
    x1 = estado[0]
    x2 = estado[1]
    x3 = estado[2]
    
    # Ecuaciones (derivadas)
    dx1_dt = x2
    dx2_dt = x3
    dx3_dt = -2*x1 - 3*x2 - 4*x3
    
    # Devolvemos las 3 derivadas en un vector de numpy
    return np.array([dx1_dt, dx2_dt, dx3_dt])


#%% SCRIPT

# cuadro comparativo (Ajustamos el encabezado para que entren las 4 columnas de datos alineadas)
print(f"{'Paso (h)':<12}{'Pasos (N)':<12}{'x1(1)':<15}{'x2(1)':<15}{'x3(1)':<15}{'Salida y(1)':<15}")


# Iteramos sobre cada paso h para calcular el resultado
for h in pasos_h:
    # Calculamos N (usamos round e int para que sea un número entero perfecto)
    N = int(round((tf - t0) / h))
    
    # llamo a la funcion (f_edo, t0, tf, x0, N)
    resultado = metodo_euler(f_edo_d, t0, tf, estado_inicial, N)
    
    # Desempaquetamos los resultados finales para poder imprimirlos por separado
    x1_final = resultado[0]
    x2_final = resultado[1]
    x3_final = resultado[2]
    
    # Calculamos la salida y usando la ecuación algebraica: y = 7*x1 - 5*x2
    y_final = 7 * x1_final - 5 * x2_final
    
    # Imprimimos la fila del cuadro
    print(f"{h:<12}{N:<12}{x1_final:<15.6f}{x2_final:<15.6f}{x3_final:<15.6f}{y_final:<15.6f}")