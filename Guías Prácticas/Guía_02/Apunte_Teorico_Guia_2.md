¡Tomamos nota! Vamos a construir un **apunte teórico completo, estructurado y sumamente claro** para que domines toda la materia del **TP2 (Espacio de Estados)**. 

Dividiremos la teoría en las **tres grandes áreas** que abarca tu guía: las ecuaciones diferenciales de primer orden (ejercicios 1 al 5), los simuladores profesionales (ejercicio 6), y el modelado y análisis matricial de espacio de estados lineales (ejercicios 7, 8 y 9) junto con la estabilidad (Clase 4 y 5).

---

### PARTE I: Ecuaciones Diferenciales de Primer Orden (Ejercicios 1 al 5)

En los primeros ejercicios del TP2 te vas a encontrar con ecuaciones donde la derivada de la variable es de primer orden (es decir, solo aparece $y'$). Para resolverlas "a mano" (de manera analítica), el método estrella que tenés que conocer es el de **Separación de Variables**.

#### 1. El Método de Separación de Variables (Tu comodín para resolver a mano)
Si tenés una ecuación diferencial de la forma:
$$\frac{dy}{dt} = g(t) \cdot h(y)$$

La regla consiste en "separar" todo lo que tenga $y$ de un lado de la igualdad y todo lo que tenga $t$ del otro lado, e integrar ambos miembros:
$$\int \frac{1}{h(y)} dy = \int g(t) dt$$

*   **Ejemplo práctico (Ejercicio 1 del TP):** $y' = y - 1$ con $y(0) = 2$.
    1.  Escribimos $y'$ como $\frac{dy}{dt}$:
        $$\frac{dy}{dt} = y - 1$$
    2.  Pasamos el término $(y-1)$ dividiendo y el $dt$ multiplicando:
        $$\frac{1}{y-1} dy = dt$$
    3.  Se integra a ambos lados:
        $$\int \frac{1}{y-1} dy = \int dt \implies \ln|y - 1| = t + C$$
    4.  Aplicamos la función exponencial ($e^x$) en ambos miembros para despejar la $y$:
        $$|y - 1| = e^{t + C} = e^t \cdot e^C \implies y(t) = 1 + K e^t$$
        *(Donde $K = e^C$ es una constante que determinamos con la condición inicial).*
    5.  Usamos $y(0) = 2$:
        $$2 = 1 + K e^0 \implies 2 = 1 + K \implies K = 1$$
    6.  **Solución analítica exacta:** $y(t) = 1 + e^t$.

#### 2. Análisis Cualitativo y Comportamiento Asintótico (Ejercicio 5)
El ejercicio 5 te pide graficar la ecuación lineal **no homogénea**:
$$y' = -y + t$$
para diferentes condiciones iniciales entre $-10$ y $10$.

La solución analítica de esta ecuación (resolviendo por factor de integración) es:
$$y(t) = t - 1 + C e^{-t}$$
Donde $C$ depende de tu condición inicial $y(0)$.

*   **¿Qué pasa cuando $t$ se hace muy grande (tiende a infinito)?**
    El término exponencial $e^{-t}$ se hace extremadamente pequeño y tiende a cero:
    $$\lim_{t \to \infty} y(t) = \lim_{t \to \infty} (t - 1 + C e^{-t}) = t - 1$$
*   **Conclusión teórica:** No importa en qué valor inicial empieces (ya sea $-10$, $0$ o $10$), a largo plazo **todas las trayectorias de simulación van a converger y pegarse a la misma recta** $y = t - 1$. Este comportamiento de convergencia a largo plazo es una muestra práctica de la **estabilidad asintótica** del sistema.

---

### PARTE II: Del Algoritmo Rústico al Solver Profesional (Ejercicio 6)

En el TP1 programaste el **Método de Euler**, que es el equivalente a ir dando pequeños pasos de simulación manual usando líneas rectas. En la ingeniería real (y en el ejercicio 6), esto no se usa porque tiene mucho error o es muy lento. 

En su lugar, se usan **Solvers de Paso Variable** (como la familia de Runge-Kutta).
*   **En MATLAB/Octave:** Usás funciones nativas como `ode45` (precisión media, ideal para sistemas normales) u `ode23` (útil si hay rigidez o querés rapidez).
*   **En Python:** La equivalencia directa es la función **`scipy.integrate.solve_ivp`**.

Para que lo tengas documentado en tu código de Python, un solucionador profesional se escribe así:
```python
from scipy.integrate import solve_ivp

# 1. Definís la ecuación diferencial f(t, y)
def f_sistema(t, y):
    return -y + t  # Ejemplo de y' = -y + t

# 2. Llamás al resolvedor pasándole: función, rango de tiempo, estado inicial y método
solucion = solve_ivp(fun=f_sistema, t_span=(0, 20), y0=[-10], method='RK45')

# t_span define el intervalo de evaluación
# solucion.t contiene los puntos de tiempo calculados
# solucion.y contiene los valores de y aproximados
```

---

### PARTE III: Representación en Espacio de Estados Lineal (Ejercicios 7, 8 y 9)

Este es el verdadero corazón de la materia y el tema central de la **Clase 2 y Clase 3**.

#### 1. Cómo reducir el orden de cualquier sistema físico (El truco de las Variables de Estado)
Cuando tenés un sistema físico con derivadas de orden alto (como el sistema masa-resorte-amortiguador del Ejercicio 8):
$$m \ddot{y}(t) + c \dot{y}(t) + k y(t) = u(t)$$

El método para pasarlo a Espacio de Estados exige **reducir el orden de las derivadas creando un sistema equivalente de ecuaciones de primer orden acopladas**.

**La regla:** Si el sistema es de orden $n$, definimos $n$ variables de estado internas. En este caso (orden 2), creamos 2 variables:
*   $x_1 = y$ (La posición del bloque)
*   $x_2 = \dot{y}$ (La velocidad del bloque)

Ahora derivamos estas nuevas variables respecto al tiempo:
*   $\dot{x}_1 = \dot{y} = x_2$
*   $\dot{x}_2 = \ddot{y}$. Despejando $\ddot{y}$ de la ecuación física original:
    $$\ddot{y} = -\frac{k}{m} y - \frac{c}{m} \dot{y} + \frac{1}{m} u(t)$$
    Reemplazamos con nuestras variables internas:
    $$\dot{x}_2 = -\frac{k}{m} x_1 - \frac{c}{m} x_2 + \frac{1}{m} u(t)$$

Esto nos permite reescribir la física en la **forma matricial estándar** (con la que trabaja toda la materia):
$$\dot{x}(t) = A x(t) + B u(t)$$
$$y(t) = C x(t) + D u(t)$$

Sustituyendo tus ecuaciones obtenés las matrices del sistema:
$$\begin{pmatrix} \dot{x}_1 \\ \dot{x}_2 \end{pmatrix} = \underbrace{\begin{pmatrix} 0 & 1 \\ -k/m & -c/m \end{pmatrix}}_{A} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \underbrace{\begin{pmatrix} 0 \\ 1/m \end{pmatrix}}_{B} u(t)$$
$$y(t) = \underbrace{\begin{pmatrix} 1 & 0 \end{pmatrix}}_{C} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \underbrace{\begin{pmatrix} 0 \end{pmatrix}}_{D} u(t)$$

*   **Matriz de Estado ($A$):** Define la dinámica interna y estabilidad del sistema.
*   **Matriz de Control ($B$):** Define cómo interactúa la entrada externa $u(t)$ con los estados internos.
*   **Matriz de Salida ($C$):** Define qué variables internas podemos medir físicamente.
*   **Matriz de Transmisión Directa ($D$):** Define el acoplamiento directo entre entrada y salida.

---

#### 2. Autovalores, Autovectores y la Solución Analítica

Para un sistema dinámico lineal autónomo (sin entrada externa, $u=0$) representado por $\dot{x} = A x$:
$$x(t) = e^{At} x_0$$

Donde **$e^{At}$** (o $\Phi(t)$) es la **Matriz de Transición de Estados**. Calcular la exponencial de una matriz no es elevar cada elemento al exponente, sino que requiere **diagonalizar la matriz $A$**.

1.  **Ecuación Característica (Hallar Autovalores $\lambda$):**
    Los autovalores representan las raíces del polinomio característico de tu matriz $A$:
    $$p(\lambda) = \det(\lambda I - A) = 0$$
2.  **Hallar Autovectores ($v$):**
    Para cada $\lambda$ calculated, buscás un vector no nulo que satisfaga:
    $$(\lambda I - A) v = 0$$
3.  **Diagonalización (Construir la solución):**
    Si tu matriz $A$ de tamaño $n \times n$ tiene $n$ autovalores distintos, es diagonalizable y se puede escribir como:
    $$A = S \Lambda S^{-1}$$
    Donde $S = \begin{pmatrix} v_1 & v_2 & \dots & v_n \end{pmatrix}$ es la matriz de autovectores y $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$ es la diagonal de autovalores.
4.  **La Solución Homogénea General:**
    La Matriz de Transición de Estados resulta ser:
    $$\Phi(t) = e^{At} = S e^{\Lambda t} S^{-1}$$
    Y la solución para cualquier estado inicial $x_0$ se expresa como una combinación lineal de los modos dinámicos del sistema:
    $$x(t) = a_1 e^{\lambda_1 t} v_1 + a_2 e^{\lambda_2 t} v_2 + \dots + a_n e^{\lambda_n t} v_n$$
    A la matriz conformada por estas soluciones independientes se la conoce como la **Matriz Fundamental de Soluciones ($\Psi(t)$)**:
    $$\Psi(t) = \begin{pmatrix} e^{\lambda_1 t} v_1 & e^{\lambda_2 t} v_2 & \dots & e^{\lambda_n t} v_n \end{pmatrix}$$

---

#### 3. Criterio de Estabilidad Interna en el Plano Complejo (Clase 4 y 5)

La ubicación de los autovalores ($\lambda = \sigma \pm i\omega$) de la matriz de estado $A$ determina completamente la estabilidad interna del sistema continuo:

| Parte Real de los Autovalores ($\text{Re}(\lambda)$) | Tipo de Comportamiento Físico | Estabilidad del Punto de Equilibrio |
| :--- | :--- | :--- |
| **Todos los $\text{Re}(\lambda) < 0$** | Las trayectorias se aproximan y "caen" hacia el punto de equilibrio (Sumidero o Foco Estable). | **Asintóticamente Estable** |
| **Algún $\text{Re}(\lambda) > 0$** | Las trayectorias se alejan al infinito (Fuente, Foco Inestable o Punto Silla). | **Inestable** |
| **Autovalores complejos puros ($\text{Re}(\lambda) = 0$)** | Las trayectorias oscilan de forma perpetua alrededor del equilibrio (Centro). | **Marginalmente Estable** |

*   **Punto Silla (Saddle Point):** Ocurre en sistemas de segundo orden cuando un autovalor es positivo (inestable) y el otro es negativo (estable). Las órbitas se acercan por un subespacio (estable) pero terminan divergiendo por el otro (inestable), salvo que arranques con condiciones iniciales perfectamente alineadas al autovector estable.

---

#### 4. Modelado Compartimental por Balance de Masa (Ejercicio 9)

El ejercicio 9 del TP2 te introduce a los **modelos compartimentales** por balance de masa (dos tanques de agua conectados en cascada).

*   **Principio físico:** La variación de masa acumulada dentro de un compartimento es igual al flujo de masa entrante menos el flujo saliente por unidad de tiempo:
    $$\dot{m} = \dot{m}_{\text{entrante}} - \dot{m}_{\text{saliente}}$$
*   **La altura del líquido como variable de estado ($x_i$):**
    La masa de agua en un tanque con área de sección transversal constante $a_i$ y altura de columna $x_i$ es:
    $$m_i(t) = \rho \cdot a_i \cdot x_i(t)$$
    Donde $\rho$ es la densidad del agua. Al derivar respecto al tiempo, la variación de masa es:
    $$\dot{m}_i(t) = \rho \cdot a_i \cdot \dot{x}_i(t)$$
*   **Balance del Tanque 1 (Área $a_1$, Nivel $x_1$):**
    *   Flujo entrante externo: $u(t)$ (caudal volumétrico). Masa entrante: $\rho \cdot u(t)$.
    *   Flujo saliente hacia el Tanque 2: Pasa por una tubería con resistencia $R_1$. El caudal es proporcional a la diferencia de alturas de líquido: $q_{12} = \frac{x_1 - x_2}{R_1}$. Masa saliente: $\rho \cdot \frac{x_1 - x_2}{R_1}$.
    *   **Ecuación de balance:**
        $$\rho \cdot a_1 \cdot \dot{x}_1 = \rho \cdot u(t) - \rho \cdot \left(\frac{x_1 - x_2}{R_1}\right)$$
        Despejando $\dot{x}_1$:
        $$\dot{x}_1 = -\frac{1}{R_1 a_1} x_1 + \frac{1}{R_1 a_1} x_2 + \frac{1}{a_1} u(t)$$

*   **Balance del Tanque 2 (Área $a_2$, Nivel $x_2$):**
    *   Flujo entrante: Caudal proveniente del Tanque 1: $q_{12} = \frac{x_1 - x_2}{R_1}$.
    *   Flujo saliente al exterior: Es proporcional a la altura de su propia columna de agua con resistencia $R_2$: $q_{out} = \frac{x_2}{R_2}$.
    *   **Ecuación de balance:**
        $$\rho \cdot a_2 \cdot \dot{x}_2 = \rho \cdot \left(\frac{x_1 - x_2}{R_1}\right) - \rho \cdot \left(\frac{x_2}{R_2}\right)$$
        Despejando $\dot{x}_2$:
        $$\dot{x}_2 = \frac{1}{R_1 a_2} x_1 - \left(\frac{1}{R_1 a_2} + \frac{1}{R_2 a_2}\right) x_2$$

Esto te da un sistema acoplado de 2 variables de estado, lineal e invariante en el tiempo, listo para representarse en matrices y simularse en Python o MATLAB.
