Para consolidar todo lo aprendido en esta primera parte de la materia y que te quede un **apunte teórico impecable**, es fundamental repasar y registrar formalmente los conceptos clave que sustentan los ejercicios del **TP1**. 


### I. Fundamentos de Sistemas y Modelado

1. **¿Qué es un Sistema?**
   * Un **sistema** es cualquier sector delimitado del universo que decidimos aislar para estudiar, permitiendo definir qué elementos están dentro y cuáles fuera, y cómo interactúa con su entorno.
   * Un sistema físico real posee infinitas variables (longitud, masa, temperatura, conductividad, etc.). Por ende, el diseñador del modelo debe seleccionar únicamente las **variables significativas** para el problema que se quiere describir.

2. **¿Qué es un Modelo Matemático?**
   * Es una aproximación formal que describe el comportamiento del sistema real mediante ecuaciones matemáticas que relacionan sus variables.
   * **Regla de oro del modelado:** **Ningún modelo es válido para todos los experimentos posibles**. Un modelo solo sirve para responder preguntas específicas bajo condiciones y experimentos determinados.

3. **Simulación Numérica (Pros y Contras)**
   * Simular consiste en codificar las ecuaciones matemáticas del modelo en un lenguaje de programación (como Python) para resolverlas computacionalmente.
   * **Ventajas:** Permite acceder a variables que físicamente son imposibles de medir, y realizar ensayos en condiciones extremas o peligrosas sin poner en riesgo el sistema real. Esto es sumamente crítico en **sistemas biomédicos** como el diseño de **marcapasos u órganos artificiales**, donde ensayar directamente en el paciente real es inviable o altamente peligroso.
   * **Desventajas:** Los resultados obtenidos son de carácter "ideal". Hay que ser sumamente precavido al usar datos simulados para predecir el comportamiento biológico real, ya que el modelo siempre simplifica la realidad.

---

### II. Clasificación de los Sistemas Dinámicos

1. **Sistemas Dinámicos (Sistemas con Memoria):**
   Un sistema es **dinámico** cuando sus variables evolucionan en el tiempo. A diferencia de los sistemas estáticos (donde la salida actual depende solo de la entrada actual), en un sistema dinámico la salida en un instante depende tanto de las entradas presentes como de la historia pasada del sistema.

2. **Clasificaciones de Modelos:**
   * **Parámetros Concentrados vs. Distribuidos:** En los modelos de **parámetros concentrados**, las variables cambian únicamente en función de una variable independiente (típicamente el tiempo $t$), modelándose con **Ecuaciones Diferenciales Ordinarias (EDO)**. En los de **parámetros distribuidos**, las variables cambian también respecto al espacio, requiriendo ecuaciones en derivadas parciales (EDP).
   * **Lineales vs. No Lineales:** Un sistema es **lineal** si cumple estrictamente con el **Principio de Superposición y Homogeneidad** (si duplicás la entrada, la salida se duplica; y la respuesta a dos entradas sumadas es la suma de sus respuestas individuales). El ejercicio 4.a (con la raíz cuadrada $\sqrt{x}$) es **no lineal**, mientras que el 4.b y el 4.d son **sistemas lineales**.
   * **Autónomos (o Homogéneos) vs. No Autónomos:** Un sistema es **autónomo** si su evolución interna no depende de entradas externas cambiantes (su entrada $u(t)$ es nula o inexistente, $B=0$ y $D=0$). Su regla de cambio no tiene el tiempo $t$ de forma explícita: $\dot{x} = f(x)$.

---

### III. Representación en el Espacio de Estados

El enfoque moderno consiste en representar un sistema de orden $n$ como un conjunto de **$n$ ecuaciones diferenciales acopladas de primer orden**. Los componentes de este modelo son:

1. **Variables de Estado ($x(t)$):**
   * Es el conjunto **mínimo** de variables internas necesarias para que, conociendo su valor en un instante inicial $t_0$ y la entrada suministrada a partir de ese momento, se pueda determinar por completo el comportamiento futuro del sistema.
   * **No necesitan ser físicamente medibles** (se eligen por conveniencia matemática).
   * Al conjunto de estas variables agrupadas se lo denomina **Vector de Estados**.

2. **Variables de Entrada ($u(t)$):**
   * Son variables externas generadas por el entorno que influyen sobre el sistema, pero que no pertenecen a él (fuerzas externas, voltajes, o el ingreso dosificado de una droga).

3. **Variables de Salida ($y(t)$):**
   * Son las variables que interactúan con el entorno exterior, útiles para observar, medir o controlar el comportamiento real del sistema. Su ecuación es puramente algebraica (no tiene derivadas).

4. **Perturbaciones:**
   * Entradas externas no deseadas e inaccesibles generadas por el entorno que afectan de forma impredecible al comportamiento del sistema.

Matemáticamente, un sistema en el espacio de estados se escribe como:
$$\dot{x}(t) = f(x(t), u(t))$$
$$y(t) = g(x(t), u(t))$$

---

### IV. Discretización y Métodos Numéricos

Dado que las computadoras funcionan con reloj de pasos discretos (puntos aislados en el tiempo), debemos transformar las ecuaciones continuas en **ecuaciones de recurrencia en diferencias finitas**.

1. **El Método de Euler:**
   Aproxima el cambio instantáneo mediante el **cociente incremental** para un paso finito de tiempo $h$:
   $$\dot{x}(t) \approx \frac{x(t+h) - x(t)}{h}$$
   Llevando al esquema iterativo que implementaste:
   $$x_{i+1} = x_i + h \cdot f(t_i, x_i)$$

2. **Error de Simulación:**
   Al aproximar una derivada (límite cuando $h \rightarrow 0$) usando un paso $h$ real, se introduce un **error de truncamiento numérico**. A menor $h$, la aproximación es más precisa, pero el procesador requiere realizar una mayor cantidad de iteraciones ($N$).

3. **Solvers Profesionales (El paso siguiente en la materia):**
   Aunque Euler es excelente para entender las bases, en la ingeniería biomédica real se utilizan algoritmos de paso variable de la familia **Runge-Kutta** (disponibles en herramientas como MATLAB o Python):
   * **`ode45`**: Solver basado en algoritmos de Runge-Kutta de orden 4 y 5. Es la opción estándar por defecto y resulta muy eficiente para sistemas "no rígidos" de precisión media.
   * **`ode23`**: Basado en Runge-Kutta de orden 2 y 3. Es sumamente útil y rápido cuando se toleran márgenes de error más aproximados o en sistemas que presentan una "rigidez moderada".
