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

---

### Ejercicio 2
> **Consigna:** *Dar 3 ventajas y 3 desventajas de usar simulaciones (o experimentos numéricos) para predecir el comportamiento de un (a) marcapasos, (b) órgano artificial.*

---

#### (a) Marcapasos Cardíaco

##### 🟢 3 Ventajas:
1. **Seguridad del Paciente (Evaluación Sin Riesgo Humano):** Permite verificar el comportamiento del algoritmo de estimulación y la respuesta ante arritmias en un entorno virtual sin exponer a pacientes a fallas eléctricas o de ritmo.
2. **Evaluación de Escenarios Extremos y de Falla:** Se pueden simular condiciones atípicas o extremas de frecuencia cardíaca (taquicardias severas, fibrilación, bloqueos AV completos, fallas del sensor) que serian altamente peligrosas o difíciles de reproducir clínicamente.
3. **Optimización de Diseño y Consumo Energético:** Permite probar y ajustar parámetros del software/hardware (duración del pulso, sensibilidad, consumo de batería) a bajo costo y en menor tiempo antes de fabricar el dispositivo físico.

##### 🔴 3 Desventajas:
1. **Simplificación del Tejido Biológico:** El modelo matemático no puede reproducir completamente la heterogeneidad, la variabilidad temporal y la electrofisiología miocárdica compleja de cada paciente individual.
2. **Incapacidad de Predecir Reacciones Inmunes/Tisulares:** No contempla fenómenos biológicos in vivo como la fibrosis alrededor del electrodo, infecciones o reacciones a cuerpo extraño.
3. **Dependencia de la Precisión del Modelo:** Si las condiciones iniciales o los parámetros del modelo son imprecisos, la simulación puede indicar estabilidad falsa cuando en la realidad el marcapasos podría fallar al detectar una arritmia real.

---

#### (b) Órgano Artificial (ej. Corazón artificial, Riñón artificial / Dializador)

##### 🟢 3 Ventajas:
1. **Reducción de Ensayos en Vivo (Ética Animal y Humana):** Minimiza la necesidad de pruebas invasivas iniciales en animales o seres humanos durante las etapas tempranas de desarrollo.
2. **Modelado Hemodinámico y Fluido-Dinámico Preciso:** Permite analizar campos de velocidad sanguínea, presiones internas y zonas de turbulencia para prevenir la formación de trombos (coágulos) o la hemólisis (destrucción de glóbulos rojos).
3. **Personalización del Diseño:** Permite ajustar la geometría y los parámetros operacionales del órgano simulado según la anatomía y tasa metabólica específica de un paciente particular antes de la cirugía.

##### 🔴 3 Desventajas:
1. **Elevada Complejidad Multifísica:** Un órgano real integra mecánica de fluidos, transporte de masa, cinética química y respuesta celular dinámica, requiriendo un costo computacional masivo y simplificaciones obligatorias.
2. **Incompatibilidad de Materiales no Predecible al 100%:** La simulación no predice con precisión absoluta la biocompatibilidad a largo plazo (degradación del material, adhesión plaquetaria, calcificación).
3. **Dificultad de Validación Experimental:** Obtener mediciones *in vivo* simultáneas de alta precisión para validar numéricamente todas las variables en el interior del dispositivo es sumamente complejo.

---

### Ejercicio 3
> **Consigna:** *Proponer 2 sistemas biomédicos: (a) dar sus variables, entradas, salidas y perturbaciones, (b) dar ventajas y desventajas de utilizar modelos y simulaciones para predecir su comportamiento.*

---

#### Sistema 1: Páncreas Artificial (Bomba de Infusión de Insulina en Lazo Cerrado)

- **(a) Variables, Entradas, Salidas y Perturbaciones:**
  - **Variables de Estado / Internas ($x$):** Concentración de glucosa en sangre ($G(t)$), concentración de insulina plasmática ($I(t)$), tasa de absorción de insulina en el tejido subcutáneo.
  - **Entrada ($u$):** Dosis/tasa de infusión continua de insulina administrada por la bomba.
  - **Salida ($y$):** Medición de la concentración de glucosa en líquido intersticial mediante el sensor continuo (CGM).
  - **Perturbaciones ($d$):** Ingesta de alimentos/carbohidratos (comidas), ejercicio físico no planificado, estrés, variaciones circadianas en la sensibilidad a la insulina.

- **(b) Ventajas y Desventajas de Modelar y Simular este Sistema:**
  - **Ventaja:** Permite sintonizar y ajustar los algoritmos de control automático (PID / MPC) para prevenir episodios severos de hipoglucemia sin poner en peligro al paciente.
  - **Desventaja:** El retardo fisiológico entre la glucosa en sangre y la glucosa en tejido intersticial cambia de persona a persona y es difícil de modelar de forma idéntica para todos los días.

---

#### Sistema 2: Ventilador / Respirador Mecánico Pulmonar

- **(a) Variables, Entradas, Salidas y Perturbaciones:**
  - **Variables de Estado / Internas ($x$):** Volumen de aire en pulmones ($V(t)$), presión alveolar ($P_{\text{alv}}$), resistencia de las vías aéreas ($R$), complacencia/elasticidad pulmonar ($C$).
  - **Entrada ($u$):** Flujo o presión de aire/oxígeno presurizado entregado por la válvula del respirador ($Q_{\text{in}}(t)$).
  - **Salida ($y$):** Presión medida en la vía aérea en la boca ($P_{\text{aw}}$), volumen corriente entregado ($V_T$), concentración de $O_2$ inspirado ($FiO_2$).
  - **Perturbaciones ($d$):** Esfuerzos respiratorios espontáneos o tos del paciente, presencia de secreciones en el tubo endotraqueal, fugas en la máscara o circuito neumático.

- **(b) Ventajas y Desventajas de Modelar y Simular este Sistema:**
  - **Ventaja:** Permite evaluar estrategias de ventilación de protección pulmonar sin arriesgar al paciente a barotrauma (daño por exceso de presión) o volutrauma (daño por exceso de volumen).
  - **Desventaja:** La mecánica pulmonar en pacientes críticos cambia rápidamente con la postura, el edema o el reclutamiento alveolar, por lo que un modelo estático no refleja la evolución continua del paciente.
