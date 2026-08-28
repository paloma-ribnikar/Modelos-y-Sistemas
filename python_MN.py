import numpy as np
import matplotlib.pyplot as plt

# <============================================================================================================================================================>
# MÉTODOS DE BÚSQUEDA DE RAÍCES
# <============================================================================================================================================================>
# 1) MÉTODO DE BISECCIÓN
# Condiciones: f continua en [a,b] y f(a)*f(b) < 0 (cumple Bolzano)
# Pasos:
# a) Calcular punto medio pm = (a+b)/2.
# b) Evaluar f(pm).
# c) Reemplazar a o b según el signo de f(pm).
# d) Repetir hasta que el error = (b - a)/2 sea menor que la tolerancia.

def biseccion(f, inter, tol):
    a = inter[0]
    b = inter[1]
    pasos = 0  # Para contar cuántas iteraciones se hicieron

    # Verifico condición del Teorema de Bolzano
    if f(a) * f(b) >= 0:
        raise ValueError("No se cumple el Teorema de Bolzano: f(a) y f(b) deben tener signos opuestos.")
        # raise detiene la ejecucion del programa y señala que ha ocurrido un error
    # BUCLE INFINITO --> Iteramos hasta cumplir con la tolerancia
    while True:
        pasos += 1
        pm = (a + b) / 2  # Punto medio
        error = (b - a) / 2  # Error --> mitad de la longitud actual del intervalo

        # Condición de parada
        # if abs(f(pm)) < tol or error < tol: pero en este caso:
        if error < tol:
            return pm, error, pasos

        # Actualizo intervalo según el signo
        if f(a) * f(pm) < 0:
            b = pm
        else:
            a = pm
    
# La raiz que obtengo es coherente con el grafico?

# 2) MÉTODO DE NEWTON-RAPHSON
# Condiciones: f derivable en un entorno de la raíz, f'(x0) != 0.
# Pasos:
# a) x_{n+1} = x_n - f(x_n)/f'(x_n)
# b) Repetir hasta que |x_{n+1}-x_n| < tol

# VENTAJAS --> CONVERGE MUCHO MAS RAPIDO QUE BISECCION (CUADRATICO), Y ES EXTENDIBLE A MAS VARIABLES
# DESVENTAJAS --> NECESITO LA DERIVADA DE LA FUNCION Y ESTA DEBE SER DERIV EN EL ENTORNO DE LA RAIZ

def newton_raphson(f, f_derivada, x0, tol, max_iter):
    
    if f_derivada(x0) == 0:
        print("No se puede aplicar Newton-Raphson: derivada nula en x0.")
        return None, 0

    iter_NR = 1  # primera iteración
    x1 = x0 - f(x0) / f_derivada(x0)  # fórmula de Newton-Raphson

    # Condición de parada: mientras no se cumpla la tolerancia
    while abs(x1 - x0) > tol and iter_NR < max_iter:
        iter_NR += 1
        x0 = x1
        if f_derivada(x0) == 0:
            print("Derivada nula en la iteración", iter_NR)
            return None, iter_NR
        x1 = x0 - f(x0) / f_derivada(x0) # actualiza el nuevo punto de partida
    
    # Mostrar error final
    print(f"Error de N-R: {abs(x1 - x0):.5e}")
    return x1, iter_NR

# RESPUESTA B: Si, el metodo de NR puede ser aplicado ya que la funcion es derivable en un entorno de la raiz buscada (requisito). Pero no
#              conviene hacerlo ya que, como fue mencionado previamente presenta limitaciones ya que Si f'(x) = 0 cerca del punto iterado (este caso), 
#              el método puede divergir. Ademas, necesita de un punto semilla bien aproximado a la raiz para destacar, y necesitaria de otro metodo
#              (biseccion), aunque se puede det. por el grafico, pero seria menos preciso.
#              Como ventaja, es un metodo que converge mucho mas rapido que biseccion, y es extendible a mas variables. Pero como contra, es necesario
#              calcular la derivada de la funcion, la cual (la func) debe ser derivable en el entorno de la raiz.

# <============================================================================================================================================================>
# INTEGRACIÓN NUMÉRICA - MÉTODOS COMPUESTOS
# <============================================================================================================================================================>
# GENERAL
# n --> Nro nodos
# subintervalos --> n - 1
# h = (b - a) / subintervalos --> paso

# OBS!! NECESITO CALCULAR X0
# Si no es FACIL de calcular analiticamente se procede de la siguiente manera:
# --> Grafico la funcion para ver aproximadamente donde corta el eje x
# --> Visualizo la primer raiz
# --> Elijo un intervalo que cumpla el Teo de Bolzano

##########################################################

# 1) TRAPECIO COMPUESTO
# Fórmula general:
# I ≈ h * [ (f(a) + f(b))/2 + Σ f(x_i) ] para i = 1..N-1
# Error teórico: |E_T| ≤ ((b - a)/12) * h^2 * max|f''(x)|

def MetodoTrapeciosCompuesto(f, a, b, h):  
 
    S=0 
 
    import numpy as np # Hay que importar numpy para poder hacer pasos 
 
    for k in np.arange(a+h,b,h):  
        S=S+f(k) # sumatoria para valores intermedios 
     
    I= h * (((f(a)+f(b))/2) + S) 
    return I 
    #Conceptualmente deberia ser np.arange(a+h,b-h,h)  
    # pero no tiene en cuenta en ultimo valor de b. Implicitamente hace b-h '''


# 2) SIMPSON COMPUESTO
# Requiere número PAR de subintervalos (N par)
# Fórmula general:
# I ≈ (h/3) * [f(a) + f(b) + 4Σ f(x_i impares) + 2Σ f(x_i pares)]
# Error teórico: |E_S| ≤ ((b - a)/180) * h^4 * max|f^{(4)}(x)|

def MetodoSimpsonCompuesto(f,a,b,h): 
     
    N = int((b - a) / h) 
    if N % 2 != 0: 
        raise ValueError("El número de subintervalos N debe ser par") 
     
    SP=0 # Suma de términos pares (multiplicados por 2) 
    SI=0 # Suma de términos impares (multiplicados por 4) 
 
    import numpy 
  
    # Sumatoria para los términos pares (multiplicados por 2) 
    for k in numpy.arange(a + 2*h, b, 2*h):  # k = a + 2h, a + 4h, ..., b - 2h 
                                             # Genera valores desde a+2h hasta b (sin incluir b), con un paso de 2h. 
        SP = SP + f(k)                                      # Esta es la suma para los términos pares 
 
    # Sumatoria para los términos impares (multiplicados por 4) 
    for k in numpy.arange(a + h, b, 2*h):  # k = a + h, a + 3h, ..., b - h 
                                           # Genera valores desde a+h hasta b (sin incluir b), con un paso de 2h. 
        SI = SI + f(k)                     # Esta es la suma para los términos impares 
         
    # Aplicamos la fórmula de Simpson compuesta 
    I = (h / 3) * (f(a) + f(b) + 2*SP + 4*SI)    
    return I

# 3) RIEMAN PUNTO MEDIO
# <==================== MÉTODO DE RIEMANN (PUNTO MEDIO) ====================>
# Genera los puntos medios de cada subintervalo
# np.linspace(a + h/2, b - h/2, nodos - 1) crea 'nodos - 1' puntos igualmente espaciados
# desde (a + h/2) hasta (b - h/2). Estos son los centros de cada subintervalo.
# x_riemann = np.linspace(a + h/2, b - h/2, nodos - 1)

# Evalúa la función w(x) en cada punto medio → obtiene la altura de cada rectángulo
# y_riemann = w(x_riemann)

# Calcula el área aproximada sumando las áreas de todos los rectángulos
# Cada rectángulo tiene ancho h y altura f(x_i*), donde x_i* es el punto medio.
# Integral ≈ h * Σ f(x_i*)
# integral_riemann = h * np.sum(y_riemann)

# Muestra el resultado final con 6 decimales
# print(f"Por Metodo de Riemann (11 Nodos): {integral_riemann:.6f}")



# <========== COTAS DE ERROR ==========>
# |E_TRAPECIO| ≤ ((b - a)/12) * h^2 * max|f''(x)|
# |E_SIMPSON| ≤ ((b - a)/180) * h^4 * max|f^{(4)}(x)|
# |E_RIEMMAN_MED| ≤ ((b - a)/24) * h^2 * max|f^{(2)}(x)|
# Voy a necesitar calcular las derivadas 2da y 4ta de la funcion, una vez que las obtengo, tengo que buscar el valor maximo absoluto de esas derivadas
# en el intervalo y luego sustituirlos en las formulas de error (en las funciones)
# Para hallar el maximo por "muestreo finito":

'''
xs = np.linspace(a, b, 200000) --> Crea un vector de 2000000 puntos igualmente espaciados entre a y b (muestreo fino del I)
max_f2 = np.max(np.abs(f2(xs)))
max_f4 = np.max(np.abs(f4(xs)))

Como funciona?:
np.abs(f2(xs)) toma el valor absoluto de cada uno (porque la fórmula del error usa el máximo del valor absoluto).
np.max(...) busca el mayor de todos esos valores.
'''
# OBS! DEBE SER POSITIVA
def error_simpson_cota(a, b, h, max_f4):
    return (b - a) / 180.0 * (h**4) * max_f4

def error_trapecio_cota(a, b, h, max_f2):
    return (b - a) / 12.0 * (h**2) * max_f2


def error_riemann_medio_cota(a, b, h, max_f2):
    return ((b - a) / 24.0) * (h**2) * max_f2 

'''
cota_trapecio = error_trapecio_cota (a, b, h, max_f2)
cota_simpson = error_simpson_cota (a, b, h, max_f4)

print ("EJERCICIO 2.2")
print("Cota |E_trap| ≤", cota_trapecio)
print("Cota |E_simp| ≤", cota_simpson)
'''
# <============================================================================================================================================================>
# INTERPOLACIÓN POLINÓMICA --> HALLO UNA FUNCION QUE PASE POR DETERMINADOS PUNTOS
# <============================================================================================================================================================>
# Pasos generales:
# 1. Definir los datos (x, y) como arrays de numpy --> DEFINO LOS DATOS DISCRETOS.
# 2. Calcular los coeficientes del polinomio con np.polyfit(x, y, grado).
# 3. Evaluar el polinomio ajustado con np.polyval(coeficientes, x_suave).
# 4. Graficar los puntos originales y la curva ajustada.
# 5. Si se necesita el área, integrar el polinomio con trapecio o Simpson.

# 0) Se importa la libreria numpy
tiempo = [0, 1, 2, 3, 5, 7]
valor = [1, 3, 8, 7, 2, 7]

# Extra: para graficar:
# La funcion plt.plot dibuja una curva uniendo los puntos (tiempo[i], valor[i]) (datos eje x, datos eje y)
# plt.plot(tiempo, valor, 'r-o', label="f(x)") 

# 1) Se definen los datos: vectores tiempo y valor --> PASO LAS LOSTAS A UN ARRAY PARA PODER USAR OPERACIONES NUMERICAS
tiempo = np.array([0, 1, 2, 3, 5, 7])
valor = np.array([1, 3, 8, 7, 2, 7])

# 2) Cuanto mayor sea el grado, más se "pega" a los puntos, pero también puede oscilar demasiado. Usamos N=3 como ajuste razonable.
grado = 5

# 3) NP.POLYFIT (X,Y,N) AJUSTA POR MINIMOS CUADRADOS UN POL DE GRADO N A LOS DATOS
coefic = np.polyfit(tiempo, valor, grado)  # --> X, Y y el número grado (grado del polinomio)
print("Coeficientes del polinomio:", coefic)

# 4) Se arma una partición fina entre 0 y 7 (muchos puntos intermedios) --> Esto permite dibujar una curva continua y suave.
t_suave = np.linspace(0, 7, 200)

# 5) Se evalúa el polinomio en esa partición fina usando polyval --> polyval usa los coeficientes y los valores de x para obtener los valores de y.
v_suave = np.polyval(coefic, t_suave)

# 6) Extra: para graficar: curva ajustada junto con los puntos originales
plt.plot(tiempo, valor, 'ko', label="Datos originales")      # puntos negros (originales)
plt.plot(t_suave, v_suave, 'c-', label=f"Ajuste polinómico (grado {grado})")

plt.title("Forma aproximada de la curva (interpolación polinómica)")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
# plt.show()

# <============================================================================================================================================================>
# SPLINE
# <============================================================================================================================================================>
# Pasos generales:
# 1. Importación: Se cargan numpy y CubicSpline de scipy.interpolate.
# 2. Entrada de Datos: Los vectores xi (coordenadas x) y fi (coordenadas y) son definidos como np.array.
# 3. Partición Fina (xFino): Se crea un vector con muchos puntos intermedios en el rango de los datos.
# 4. Generación del Spline: El comando spl = CubicSpline(xi, fi) resuelve el complejo sistema de ecuaciones para construir los polinomios de tercer grado que unen los segmentos con continuidad C2
# 5. Evaluación (yfino): El objeto spl se utiliza como una función para calcular los valores interpolados en la partición fina.
# 6. Graficación: Se usa plt.plot() para mostrar los puntos originales y la curva suave generada por el spline.

import numpy as np                               # Para manejo de vectores [5]
from scipy.interpolate import CubicSpline          # Función específica para Spline Cúbico [1]
import matplotlib.pyplot as plt                  # Para graficación [6, 7]

# ==============================================================================
# 1. DEFINICIÓN DE LOS DATOS DE ENTRADA
# ==============================================================================

# Puntos de datos (xi, fi) a interpolar [4]
# Vector de coordenadas x (xi)
xi = np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5, 6.0,
               7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])

# Vector de coordenadas y (fi)
fi = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1,
               2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])

# ==============================================================================
# 2. GENERACIÓN Y EVALUACIÓN DEL SPLINE
# ==============================================================================

# Paso 2A: Definición de la partición fina (xFino) para la graficación.
# Usamos np.arange para generar un punto cada 0.1, desde 0.9 hasta 13.3 [2].
# Se incluye 13.4 para asegurar que el límite final 13.3 esté cubierto [8].
xFino = np.arange(0.9, 13.4, 0.1)

# Paso 2B: Creación del objeto Spline. 
# El comando CubicSpline toma los datos (xi, fi) y genera la función S(x) a trozos.
spl = CubicSpline(xi, fi) # El nombre 'spl' se puede cambiar [2]

# Paso 2C: Evaluación del Spline. 
# El objeto 'spl' se evalúa en el vector xFino, generando los valores yfino.
yfino = spl(xFino) # Evaluación del objeto spline [2]

# ==============================================================================
# 3. VISUALIZACIÓN DE RESULTADOS
# ==============================================================================

# Trazado de los puntos originales y la curva interpolada.
plt.figure(figsize=(10, 6))

# Graficamos los puntos originales (xi, fi) usando círculos ('o') para mostrarlos [9]
plt.plot(xi, fi, 'o', label='Puntos Originales') 

# Graficamos la curva spline (xFino, yfino) usando una línea continua ('-') [2]
plt.plot(xFino, yfino, '-', label='Spline Cúbico')

plt.title("Interpolación por Spline Cúbico (Pato en Vuelo)")
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")
plt.grid(True) # Agrega una grilla [7]
# plt.show() # Muestra el gráfico generado [6, 7]


# <============================================================================================================================================================>
# SISTEMAS DE ECUACIONES DIFERENCIALES - MÉTODO DE EULER
# <============================================================================================================================================================>
# Ejemplo genérico de implementación de Euler explícito para un sistema de 2 EDOs:
# dy/dt = f1(t, y, z)
# dz/dt = f2(t, y, z)
#
# Pasos:
# 1. Definir las ecuaciones dentro de una función f(t, y, z) que devuelva un array [dy/dt, dz/dt].
# 2. Definir condiciones iniciales y parámetros (t0, tf, N, h).
# 3. Implementar el bucle de Euler: y_{k+1} = y_k + h * f(t_k, y_k, z_k).
# 4. Graficar las soluciones.

def euler_sistema(f, t0, tf, N, y0, z0):
    h = (tf - t0) / N
    t = np.arange(t0, tf + h, h)
    y = np.zeros((2, N + 1))
    y[0, 0] = y0
    y[1, 0] = z0
    for k in np.arange(0, N):
        y[:, k + 1] = y[:, k] + h * f(t[k], y[0, k], y[1, k])
    return t, y


# Ejemplo de uso:
# f = lambda t, y, z: np.array([-0.2 * np.cos(3 * y), 0.1 * y + 2 * np.sin(2 * z)])
# t, y = euler_sistema(f, 0, 2, 20, 2, 1)
# plt.plot(t, y[0, :], 'r', label='y(t)')
# plt.plot(t, y[1, :], 'b', label='z(t)')
# plt.legend(); plt.show()

# ===============================================================
# METODO DE EULER
# ===============================================================
# La ecuacion diferencial me dice la pendiente en cada punto --> y'=f(t,y), Euler aproxima la sol paso a paso:
# toma la pendiente actual y avanza un pedacito h
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

''' # 1. Euler con un solo paso (N=1)
h_1 = T / 1
y_euler_1 = metodo_euler(f_edo, t0, tf, y0, N=1)

# 2. Euler con cuatro pasos (N=4)
y_euler_4 = metodo_euler(f_edo, t0, tf, y0, N=4) '''

# ===============================================================
# METODO DE HEUN
# ===============================================================
# Heun mejora a Euler porque en lugar de seguir solo la pendiente inicial,
# promedia la pendiente inicial y la final del tramo → se corrige la predicción.
# Suaviza el error y da una mejor aproximacion, ademas, converge mas rapido

def metodo_heun(f, t0, tf, y0, N):
    """Implementación del Método de Heun (RK2)"""
    h = (tf - t0) / N
    t, y = t0, y0
    for _ in range(N):
        # K1 (F1k)
        F1k = f(t, y)
        
        # K2 (F2k) - Usa el predictor y_k + h*F1k
        F2k = f(t + h, y + h * F1k)
        
        # Corrección (Promedio de pendientes)
        y = y + (h / 2) * (F1k + F2k)
        t = t + h
    return y

'''# 3. Heun con un solo paso (N=1)
y_heun_1 = metodo_heun(f_edo, t0, tf, y0, N=1)

# 4. Heun con cuatro pasos (N=4)
y_heun_4 = metodo_heun(f_edo, t0, tf, y0, N=4)'''


'''
print("\n--- Resultados numéricos ---")
print(f"Euler (1 paso): {y_euler_1:.6f}")
print(f"Euler (4 pasos): {y_euler_4:.6f}")
print(f"Heun  (1 paso): {y_heun_1:.6f}")
print(f"Heun  (4 pasos): {y_heun_4:.6f}")
'''

# <============================================================================================================================================================>
# GRAFICO
# <============================================================================================================================================================>
# Grafico la funcion g
# Intervalo
inter = [0, 9/5]
a = inter[0]
b = inter[1]

# x = np.linspace (inter [0], inter [1],2000) # NP.LINSPACE CREA LISTAS DE VALORES --> (INICIO, FIN CANTIDAD). PUNTOS EQUIESPACIADOS, SIRVE PARA QUE EL GRAF SEA SUAVE
# y = g(x) # CALCULA EL VALOR DE Y EN CADA UNO DE ESOS PUNTOS
# plt.plot (x, y, 'gray', label = "f(x)") #LABEL PARA QUE APAREZCA EN LA LEYENDA

###################################################
# Ejes
# plt.axhline(0, color='k', linestyle='--')   # eje x
# plt.axvline(0, color='k', linestyle='--')   # eje y


# plt.title("Grafico")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.6)
##################################################
# plt.show()

# <============================================================================================================================================================>
# EXTRA
# <============================================================================================================================================================>
# Para limpiar la pantalla:
import os 
os.system('cls' if os.name == 'nt' else 'clear')


# compuesto usando vectores
# -> para los impares arranca en el primer y llega hasta el ultimo(-1)->los pares arrancan del 2 hasta el penultimo(-2)
# el ultimo argumeto de sum es el paso, ada cuanto avanza
def simpson_13_compuesto(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("Simpson 1/3 compuesto requiere N par.")
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    I = (h / 3.0) * (
        y[0]
        + y[-1]
        + 4.0 * np.sum(y[1:-1:2])  # índices impares: 1,3,5,...
        + 2.0 * np.sum(y[2:-2:2])
    )  # índices pares internos: 2,4,6,...
    print(f"[SIMPSON 1/3 COMP] N={N}  I ≈ {I:.10f}")
    return I

def simpson_vect(t, y):
    N = len(t) - 1
    h = t[1] - t[0]

    return (h/3) * (
        y[0]
        + y[-1]
        + 4*np.sum(y[1:-1:2])      # impares
        + 2*np.sum(y[2:-2:2])      # pares internos
    )


# otra forma(codigo del libro)

#h = (b-a)/N
def simpson_13_compuesto_libro(f, a, b, h):
    N = int((b - a) / h)
    if N % 2 != 0:
        raise ValueError("Simpson 1/3 compuesto requiere N par (N=(b-a)/h).")

    SP = 0.0  # términos pares: a+2h, a+4h, …
    SI = 0.0  # términos impares: a+h, a+3h, …

    for k in np.arange(a + 2 * h, b, 2 * h):
        SP += f(k)
    for k in np.arange(a + h, b, 2 * h):
        SI += f(k)

    I = (h / 3.0) * (f(a) + f(b) + 2.0 * SP + 4.0 * SI)
    print(f"[SIMPSON 1/3 COMP (h)] h={h:g}  I ≈ {I:.10f}")
    return I
