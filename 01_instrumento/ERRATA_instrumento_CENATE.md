# Nota de erratas del instrumento CENATE (versión aplicada)

> Corresponde al **Apéndice A, punto A.1** del Trabajo Fin de Máster.
> Debe leerse conjuntamente con el instrumento aplicado (`Apendice_A_Instrumento_CENATE_v10.pdf`)
> y con el manual de cumplimentación (`../02_manual_glosario/`).

La comparación entre el formulario efectivamente aplicado y la especificación metodológica del Capítulo 3 identificó **cinco discrepancias** de redacción o de instrucciones. Las cuatro primeras no alteraron las respuestas obtenidas ni el cálculo de los índices; la quinta afecta a las instrucciones de cumplimentación de los campos numéricos del Bloque C y exigió un tratamiento previo de los datos.

El registro de estas discrepancias garantiza la trazabilidad del instrumento, explica los procedimientos adoptados y orienta las correcciones para una posible segunda ronda.

---

## A.1.1 — Primera discrepancia: número de variables e indicadores del Bloque C

El texto introductorio del formulario indica que el cuestionario contiene «aproximadamente 39 variables cuantitativas y 23 ítems binarios que sustentan los 30 KPI». Se trata de una redacción heredada de una versión anterior e imprecisa.

**Situación real del instrumento aplicado:**

| Elemento | Cantidad real |
|---|---|
| Variables cuantitativas (grupos C1 a C11) | **61** |
| Ítems binarios (sección C12) | **23** |
| Indicadores especificados en el diccionario | **15** |
| Indicadores calculados en esta aplicación | **14** |
| Indicadores considerados suficientemente comparables | **12** |

**Efecto:** ninguno sobre las respuestas ni sobre el cálculo del IMI, el IPR o el IEI.

---

## A.1.2 — Segunda discrepancia: referencia inexistente en el grupo C2

Las instrucciones del grupo C2 remiten a un «ítem C2.12» que no existe: el grupo consta de cuatro variables (C2.1 a C2.4).

**Referencia correcta:** el campo de comentarios generales del Bloque C.

**Efecto:** ninguno sobre los cálculos.

---

## A.1.3 — Tercera discrepancia: extensión de los enunciados del Bloque B

La nota introductoria indica correctamente que los descriptores de calibración corresponden a los niveles 1, 3 y 5 de la escala. Sin embargo, algunos enunciados resultaron excesivamente extensos para su lectura cómoda en plataforma electrónica.

**Efecto:** no altera la estructura de los ítems ni los cálculos. Su revisión forma parte de la Propuesta 4 (Sección 7.4 del TFM).

---

## A.1.4 — Cuarta discrepancia: término «bianual» en el ítem E6

El ítem E6 emplea el término «bianual», que en español admite doble interpretación (dos veces al año / cada dos años).

**Periodicidad efectivamente propuesta para el CENATE:** **bienal** (cada dos años), conforme a la Sección 4.4 y a la Propuesta 1 del TFM.

**Efecto:** la ambigüedad quedó atenuada por el contexto, ya que el ítem contrapone explícitamente esa periodicidad a la realización anual. El término deberá corregirse antes de una segunda ronda.

---

## A.1.5 — Quinta discrepancia: cumplimentación de datos numéricos no disponibles

**Esta es la única discrepancia con efecto sobre el tratamiento de los datos.**

El ítem 3 de las instrucciones generales indica registrar «0 (cero)» cuando un dato numérico no esté disponible. Esto difiere de la convención establecida en la Sección 3.6 del TFM y en el diccionario de variables, según la cual todo dato no disponible debe registrarse como **ND** y excluirse del cálculo.

El uso del cero genera ambigüedad, porque no permite distinguir:

- un valor observado que efectivamente es igual a cero, de
- la ausencia de información.

**Procedimiento adoptado.** Antes de los cálculos se reclasificaron como «ND» los valores cero incompatibles con la existencia o el funcionamiento de una administración tributaria, a saber: plantilla, recaudación, contribuyentes activos y declaraciones previstas. Cada reclasificación quedó consignada en el registro de tratamiento y, cuando fue posible, se remitió a la unidad informante para su confirmación.

**Casos afectados** (identificados con código neutro, conforme al protocolo de seudonimización de la Sección 3.9):

- Una administración cumplimentó con cero **47 variables** monetarias, de efectivos o de recuento. La unidad informante confirmó posteriormente que se trataba de **información no disponible**, y no de valores nulos. El tratamiento adoptado quedó así ratificado y ningún índice se alteró.
- Otra administración registró cero en las seis variables iniciales del cuaderno cuantitativo y dejó el resto sin cumplimentar; ninguna de sus variables cuantitativas se consideró utilizable.

**Regla de tratamiento del cero, aplicada de forma uniforme:** un cero en una variable de nivel (monetaria, de efectivo o de recuento) se trata como *no informado*, en razón de la instrucción del formulario que orientaba a cumplimentar con cero en ausencia del dato.

**Corrección prevista.** La uniformización de esta norma forma parte de la Propuesta 5 (Sección 7.4 del TFM): en futuras aplicaciones, los campos no disponibles deberán registrarse exclusivamente como «ND», con validaciones de plausibilidad en el momento de la cumplimentación que preserven los valores nulos sustantivamente posibles.

---

## Resumen del efecto sobre los índices

| Discrepancia | ¿Afecta a las respuestas? | ¿Afecta a IMI / IPR / IEI? |
|---|---|---|
| A.1.1 — Número de variables | No | No |
| A.1.2 — Referencia C2.12 | No | No |
| A.1.3 — Extensión de enunciados | No | No |
| A.1.4 — Término «bianual» | No | No |
| A.1.5 — Cero como dato no disponible | **Sí** | No (tras la reclasificación a ND) |

Las cuatro primeras discrepancias son de redacción. La quinta exigió tratamiento previo de los datos, documentado en la Sección 5.2.2 del TFM y en el registro de tratamiento incluido en este repositorio.
