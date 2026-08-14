# Resumen Integrado - Clase 1 y Clase 2: Modelos y Sistemas
*Consolidado de Diapositivas Oficiales (Prof. Diana Rubio), Resumen 2024 y Apuntes de Clase*

---

## 📌 CLASE 1: Introducción a Sistemas y Modelos

### 1. Definición de Sistema
- **Definición General (Gaines, 1979):** Cualquier fragmento del universo que aislemos para definir qué está *dentro* y qué está *fuera* constituye un sistema. Está caracterizado por sus límites y por la forma en que interactúa con su entorno.
- **Lista de Variables (Ashby, 1956):** Un sistema puede definirse como una lista de variables de interés. *(Nota: Todo objeto real posee infinitas variables; quien diseña el modelo selecciona las variables relevantes para el problema).*
- **Conjunto de Elementos Interconectados:** Es una colección de componentes enlazados entre sí que interactúan bajo determinadas leyes (físicas, biológicas, químicas, sociales, económicas) para cumplir una función específica.

> ✏️ **Anotación de Clase / Ejemplos:**
> - *Ejemplo biológico:* Sistema digestivo, sistema circulatorio (las arterias actúan como **filtros pasa bajos**: convierten un flujo pulsátil del corazón en un flujo continuo sanguíneo).
> - *Ejemplo no biológico:* Partes de un equipamiento, circuito eléctrico RC con batería (donde interesan los voltajes en R y C).

---

### 2. Elementos de un Sistema y Clasificación de Variables

| Tipo de Variable | Definición | Ejemplo |
| :--- | :--- | :--- |
| **Variables Internas / de Estado ($x$)** | Describen el comportamiento interno del sistema y sus interacciones. | Posición, velocidad, concentración de droga en estómago/sangre, voltaje en capacitor. |
| **Variables de Entrada ($u$ / Inputs)** | Variables externas generadas por el entorno que influyen en el sistema. | Fuerza externa aplicada, dosis de medicamento ingresada, voltaje de fuente. |
| **Variables de Salida ($y$ / Outputs)** | Variables observables/medibles del sistema determinadas por los estados y entradas. | Altura de columna de Hg, medición en análisis de sangre, posición de masa. |
| **Perturbaciones ($d$)** | Entradas inaccesibles o no controlables del mundo exterior. | Ruido térmico, variaciones ambientales, imprecisiones de medición. |

---

### 3. Experimento y Modelado
- **Experimento:** Proceso de extracción de datos mediante la aplicación de condiciones iniciales, variación de entradas y registro de respuestas.
- **Simulación Numérica:** Ensayos experimentales previos por computadora para verificar qué tan bien un modelo matemático representa al sistema real antes de construirlo o probarlo físicamente.
- **Modelo Matemático:** Conjunto de ecuaciones (diferenciales, algebraicas, de diferencias) que relacionan las variables del sistema.
- **Propiedad Fundamental:** *Ningún modelo es válido para todos los experimentos posibles.* Se busca el modelo más simple que responda las preguntas de interés.

---

### 4. Clasificación de los Modelos Matemáticos

1. **Determinísticos vs. Estocásticos:**
   - *Determinístico:* A entradas iguales corresponden siempre salidas iguales (no hay incertidumbre).
   - *Estocástico:* Intervienen variables aleatorias o probabilidades.
2. **Continuos vs. Discretos:**
   - *Continuo:* El intervalo de tiempo $T$ es continuo en $\mathbb{R}$ (ej. $T = [0, \infty)$). Se describe con Ecuaciones Diferenciales Ordinarias (**ODE**).
   - *Discreto:* El tiempo $T$ toma valores aislados (ej. $T \in \mathbb{Z}, \mathbb{N}$). Se describe con Ecuaciones en Diferencias.
3. **Autónomos vs. No Autónomos:**
   - *Autónomo:* Las ecuaciones no dependen explícitamente del tiempo $t$ ni de entradas externas variables.

---

## 📌 CLASE 2: Sistemas Dinámicos y Espacio de Estados

### 1. Representación en el Espacio de Estados

La representación en espacio de estados de un sistema dinámico continuo de orden $n$ se compone de:

1. **Ecuación de Estado (dinámica interna):**
   $$\dot{x}(t) = f(x(t), u(t), t)$$
2. **Ecuación de Salida (medición/observación):**
   $$y(t) = h(x(t), u(t), t)$$

Donde:
- $x(t) = [x_1(t), x_2(t), \dots, x_n(t)]^T \in \mathbb{R}^n$ es el **vector de estados** (mínimo número de variables requeridas para describir completamente el estado del sistema en cualquier instante $t$).
- $u(t) \in \mathbb{R}^m$ es el vector de entradas (controles).
- $y(t) \in \mathbb{R}^p$ es el vector de salidas.

> ⚡ **Propiedad Clave (Unicidad):** La representación de un sistema en el espacio de estados **NO ES ÚNICA**. Existen infinitas selecciones válidas para los estados mediante transformaciones lineales de coordenadas ($z = Px$).

---

### 2. Sistemas Lineales e Invariantes en el Tiempo (LTI)

Para sistemas LTI de dimensión finita, el modelo matricial es:

$$\begin{cases} \dot{x}(t) = A x(t) + B u(t) \\ y(t) = C x(t) + D u(t) \end{cases}$$

- $A \in \mathbb{R}^{n \times n}$: Matriz de Estado (dinámica del sistema).
- $B \in \mathbb{R}^{n \times m}$: Matriz de Entrada (control).
- $C \in \mathbb{R}^{p \times n}$: Matriz de Salida (observación).
- $D \in \mathbb{R}^{p \times m}$: Matriz de Transmisión Directa (feedthrough).

---

### 3. Ejemplos Emblemáticos de Cursada

#### Ejemplo 1: Absorción de Medicamento (Farmacocinética - 1er y 2do Orden)
- **1er Orden (solo estómago):**
  $$\dot{x}_1(t) = -k_1 x_1(t) + u(t)$$
  $x_1(t)$: concentración en estómago, $u(t)$: dosis ingresada.

- **2do Orden (estómago + sangre):**
  $$\begin{cases} \dot{x}_1(t) = -k_1 x_1(t) + u(t) \\ \dot{x}_2(t) = k_1 x_1(t) - k_2 x_2(t) \end{cases}$$
  $x_2(t)$: concentración en sangre.

  Forma matricial:
  $$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} -k_1 & 0 \\ k_1 & -k_2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 1 \\ 0 \end{bmatrix} u(t)$$

#### Ejemplo 2: Sistema Masa-Resorte-Amortiguador (2do Orden)
Ecuación física ($2^{\text{da}}$ ley de Newton): $m \ddot{x}(t) + b \dot{x}(t) + k x(t) = u(t)$.

Reducción de orden seleccionando estados: $x_1(t) = x(t)$ (posición), $x_2(t) = \dot{x}(t)$ (velocidad).
$$\begin{cases} \dot{x}_1 = x_2 \\ \dot{x}_2 = -\frac{k}{m} x_1 - \frac{b}{m} x_2 + \frac{1}{m} u(t) \end{cases}$$

---

### 4. Discretización de Modelos Continuos (Método de Euler)

Para simulación numérica o implementación digital, aproximamos la derivada continua $\dot{x}(t) \approx \frac{x_{k+1} - x_k}{h}$ (donde $h = \Delta t$ es el paso de integración):

$$x_{k+1} = x_k + h f(x_k, u_k)$$

Para el sistema LTI autónomo ($\dot{x} = Ax$):
$$x_{k+1} = (I + hA) x_k$$

> ✏️ **Anotación de Clase:** El Método de Euler permite resolver el sistema tanto **analíticamente** (paso a paso) como **numéricamente** por simulación en computadora.

---

### 5. Resumen de Conceptos Clave para el Parcial
1. **Reducción de Orden:** Toda EDO de orden $n$ se convierte en un sistema de $n$ EDOs de 1er orden definiendo $x_1 = y, x_2 = \dot{y}, \dots, x_n = y^{(n-1)}$.
2. **Dimensiones:** $n$ es el orden del sistema (# de variables de estado), $m$ es el # de entradas, $p$ es el # de salidas.
3. **Análisis Cualitativo vs Quantitative:** En espacio de estados interesa tanto el valor exacto como la trayectoria cualitativa (estabilidad, régimen permanente, comportamiento asintótico).
