import numpy as np

def metodo_euler_vectorial(f_edo, t0, tf_eval, V0, N):
    """
    Método de Euler para sistemas vectoriales de EDOs.
    f_edo: función dy/dt = f(t, V) que retorna un array de derivadas
    t0: tiempo inicial (0)
    tf_eval: tiempo final hasta donde integrar (t0 dado en la consigna)
    V0: vector de condiciones iniciales en t=0 (np.array)
    N: número de pasos de integración
    """
    h = (tf_eval - t0) / N
    t = t0
    V = np.array(V0, dtype=float)
    
    for _ in range(N):
        V = V + h * np.array(f_edo(t, V), dtype=float)
        t = t + h
        
    return V

# =============================================================================
# EJERCICIO 4 (b)
# dx/dt = y
# dy/dt = x - y
# x(0) = 1, y(0) = 2, t0 = 1
# =============================================================================
def f_edo_b(t, V):
    x, y = V[0], V[1]
    dx_dt = y
    dy_dt = x - y
    return [dx_dt, dy_dt]

# =============================================================================
# EJERCICIO 4 (c)
# dx1/dt = x2
# dx2/dt = cos(10 * pi * x1)
# y = x1
# x1(0) = 0, x2(0) = 1, t0 = 1
# =============================================================================
def f_edo_c(t, V):
    x1, x2 = V[0], V[1]
    dx1_dt = x2
    dx2_dt = np.cos(10 * np.pi * x1)
    return [dx1_dt, dx2_dt]

# =============================================================================
# EJERCICIO 4 (d)
# dx1/dt = x2
# dx2/dt = x3
# dx3/dt = -2*x1 - 3*x2 - 4*x3
# y = 7*x1 - 5*x2
# x1(0) = 2, x2(0) = 1, x3(0) = 0, t0 = 1
# =============================================================================
def f_edo_d(t, V):
    x1, x2, x3 = V[0], V[1], V[2]
    dx1_dt = x2
    dx2_dt = x3
    dx3_dt = -2*x1 - 3*x2 - 4*x3
    return [dx1_dt, dx2_dt, dx3_dt]


# --- EJECUCIÓN Y TABLAS COMPARATIVAS ---
pasos_h = [0.5, 0.1, 0.05]
t_inicio = 0.0
tf_eval = 1.0  # t0 = 1 según la consigna

print("=" * 65)
print("EJERCICIO 4 (b): x'(t) = y,  y'(t) = x - y")
print(f"Condiciones iniciales: x(0)=1, y(0)=2 | Evaluado en t0 = {tf_eval}")
print("=" * 65)
print(f"{'Paso (h)':<12}{'Pasos (N)':<12}{'x(1)':<20}{'y(1)':<20}")
print("-" * 65)

for h in pasos_h:
    N = int(round((tf_eval - t_inicio) / h))
    V_res = metodo_euler_vectorial(f_edo_b, t_inicio, tf_eval, [1.0, 2.0], N)
    print(f"{h:<12}{N:<12}{V_res[0]:<20.6f}{V_res[1]:<20.6f}")

print("\n" + "=" * 65)
print("EJERCICIO 4 (c): x1' = x2,  x2' = cos(10*pi*x1)")
print(f"Condiciones iniciales: x1(0)=0, x2(0)=1 | Salida y = x1 | Evaluado en t0 = {tf_eval}")
print("=" * 65)
print(f"{'Paso (h)':<12}{'Pasos (N)':<12}{'x1(1) = y(1)':<20}{'x2(1)':<20}")
print("-" * 65)

for h in pasos_h:
    N = int(round((tf_eval - t_inicio) / h))
    V_res = metodo_euler_vectorial(f_edo_c, t_inicio, tf_eval, [0.0, 1.0], N)
    print(f"{h:<12}{N:<12}{V_res[0]:<20.6f}{V_res[1]:<20.6f}")

print("\n" + "=" * 65)
print("EJERCICIO 4 (d): Sistema de 3er Orden LTI")
print("x1' = x2,  x2' = x3,  x3' = -2*x1 - 3*x2 - 4*x3")
print(f"Condiciones iniciales: x1(0)=2, x2(0)=1, x3(0)=0 | Salida y = 7*x1 - 5*x2 | t0 = {tf_eval}")
print("=" * 65)
print(f"{'Paso (h)':<12}{'Pasos (N)':<12}{'x1(1)':<15}{'x2(1)':<15}{'x3(1)':<15}{'Salida y(1)':<15}")
print("-" * 65)

for h in pasos_h:
    N = int(round((tf_eval - t_inicio) / h))
    V_res = metodo_euler_vectorial(f_edo_d, t_inicio, tf_eval, [2.0, 1.0, 0.0], N)
    y_out = 7 * V_res[0] - 5 * V_res[1]
    print(f"{h:<12}{N:<12}{V_res[0]:<15.6f}{V_res[1]:<15.6f}{V_res[2]:<15.6f}{y_out:<15.6f}")
