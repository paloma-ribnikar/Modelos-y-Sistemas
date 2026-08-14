# Práctica 1: Sistemas - Modelos y Sistemas (UNSAM)

---

## 📚 1. Marco Teórico Introductorio (Basado en Apuntes de Clase)

### ¿Qué es un Sistema?
Un **sistema** es un conjunto de elementos enlazados o interconectados entre sí que interactúan organizadamente para **cumplir una función específica**.

### Ejemplos de Sistemas:
- **Ejemplo Biológico:** El *sistema digestivo* (conjunto de órganos interconectados que procesan y absorben nutrientes).
- **Ejemplo Ingenieril / Técnico:** Las partes y componentes interconectados de un *equipamiento o maquinaria*.
- **Ejemplo Fisiológico / Circulatorio (Arterias):** Las arterias funcionan como un **filtro pasa bajos**; su objetivo fisiológico es transformar un flujo sanguíneo **pulsátil** (generado por los latidos del corazón) en un flujo **constante y continuo** a través de los capilares y tejidos.

### El Propósito del Modelado y la Simulación
- **Modelado:** Se busca construir modelos matemáticos para **describir, analizar y predecir el comportamiento** de un sistema.
- **Simulación Numérica:** Consiste en realizar *ensayos experimentales previos por computadora* para verificar **qué tan bien funciona la idea o el modelo** antes de implementarlo físicamente.
- **Variables Externas / Perturbaciones:** Son variables provenientes del entorno que **no se pueden controlar**, pero que influyen en la dinámica del sistema.

---

## 📝 2. Resolución de Ejercicios

### Ejercicio 1
> **Consigna:** *Para los siguientes sistemas, determinar las variables, identificar las entradas, las salidas y las perturbaciones (donde sea aplicable):*

---

#### (a) Un Termómetro 🌡️

- **Variables de Estado / Internas ($x$):**
  - Temperatura interna de la sustancia o sensor termométrico ($T_{\text{term}}$).
  - Volumen / dilatación de la sustancia (mercurio/alcohol) o resistencia eléctrica interna (en sensores digitales).
- **Entrada ($u$):**
  - Temperatura del cuerpo o medio exterior con el cual se pone en contacto ($T_{\text{medio}}$).
- **Salida ($y$):**
  - Lectura visual de la temperatura en la escala graduada (o valor numérico en la pantalla digital).
- **Perturbaciones ($d$):**
  - Temperatura del aire ambiente (si el contacto no es perfecto).
  - Tiempo insuficiente de medición.
  - Transferencia de calor secundaria hacia las manos de quien sostiene el termómetro.

---

#### (b) Un Electrocardiograma (ECG) 🫀

- **Variables de Estado / Internas ($x$):**
  - Actividad eléctrica / potenciales de acción de las células del miocardio.
  - Carga / voltaje acumulado en los electrodos y en los circuitos de filtrado y amplificación del equipo.
- **Entrada ($u$):**
  - Señal eléctrica cardíaca nativa (procesos de despolarización y repolarización del corazón).
- **Salida ($y$):**
  - Trazado de las ondas cardíacas ($P, QRS, T$) graficado en pantalla o impreso en papel milimetrado.
- **Perturbaciones ($d$):**
  - Artefactos por movimiento del paciente o contracción de otros músculos (ruido electromiográfico).
  - Interferencia electromagnética de la red eléctrica (50 Hz / 60 Hz).
  - Variación en la impedancia de contacto de los electrodos sobre la piel (sudor, vello, desprendimiento).

---

#### (c) Un Crecimiento Bacteriano 🧫

- **Variables de Estado / Internas ($x$):**
  - Población o cantidad de bacterias ($N(t)$) / Biomasa total acumulada.
  - Concentración de nutrientes internos y metabolitos en el cultivo.
- **Entrada ($u$):**
  - Suministro externo de nutrientes (sustrato / glucosa).
  - Suministro de oxígeno o flujo de alimentación de medio de cultivo.
- **Salida ($y$):**
  - Densidad óptica del cultivo (medida con espectrofotómetro) o recuento de unidades formadoras de colonias (UFC).
  - Concentración de un producto metabólico secundario de interés.
- **Perturbaciones ($d$):**
  - Variaciones no deseadas de temperatura en la incubadora.
  - Contaminación por otros microorganismos o bacteriófagos.
  - Cambios de pH no controlados o acumulación de desechos metabólicos tóxicos.
