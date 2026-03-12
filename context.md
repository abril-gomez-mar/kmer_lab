# Descripción del proyecto.

### 1. Problema
Obtener todos los kmers de una secuencia de ADN brindada por el usuario. El valor k también es un input.

**Segunda versión del problema**

Además de generar todos los k-mers, ahora queremos evaluar cada uno para determinar cuál tiene mayor contenido GC.

**Problema ampliado**
Además de generar k-mers y encontrar el mejor por contenido GC, ahora queremos visualizar el proceso de recorrido de la secuencia con una ventana deslizante.

<br>

### 2. Datos de entrada

-Una secuencia de DNA introducida por el usuario.
-Un número entero k que representa el tamaño del k-mer.

<br>

### 3. Requisitos funcionales

-Leer una secuencia de DNA.
-Leer el valor de k.
-Recorrer la secuencia.
-Generar todos los k-mers de longitud k.
-Mostrar cada k-mer en pantalla.

*Nuevos requisitos*
- Calcular cuántos nucleótidos G o C tiene cada k-mer.
- Comparar el valor GC de cada k-mer con el mejor encontrado hasta el momento.
- Guardar el mejor k-mer.
- Guardar la posición donde aparece.
- Mostrar al final el mejor resultado encontrado.

**Requisitos de la extensión final del programa**
-Mostrar la secuencia completa en cada iteración.
-Mostrar una línea visual que indique la posición actual de la ventana de tamaño k.
-Alinear esa visualización con el k-mer que se está evaluando.

<br>

### 4. Requisitos no funcionales

-El programa debe aceptar secuencias en mayúsculas o minúsculas.
- La secuencia debe convertirse a mayúsculas.
- El código debe ser legible y seguir convenciones básicas de estilo, según PEP-8.

<br>

### 5. Algoritmo

1. Leer la secuencia de DNA.
2. Leer el valor de k.
3. Recorrer la secuencia desde la posición 0 hasta len(seq) - k.
4. En cada posición, extraer un fragmento de longitud k.
5. Mostrar el k-mer generado.

*Nuevo algoritmo*
1. Leer la secuencia de DNA.
2. Leer el valor de k.
3. Preparar variables para guardar el mejor resultado encontrado hasta el momento.
4. Recorrer la secuencia usando una ventana de tamaño k.
5. Obtener el k-mer de la posición actual.
6. Contar cuántas letras G o C tiene ese k-mer.
7. Mostrar el k-mer actual junto con su valor GC.
8. Comparar ese valor con el mejor valor guardado.
9. Si el k-mer actual tiene mayor contenido GC, actualizar el mejor resultado.
10. Mostrar el mensaje Best so far con el mejor k-mer registrado hasta ese momento.
11. Al final, mostrar el mejor k-mer, su posición y su contenido GC.

*Algoritmo de la tercera versión del programa*
1. Leer la secuencia de DNA.
2. Leer el valor de k.
3. Preparar variables para guardar el mejor resultado encontrado hasta el momento.
4. Recorrer la secuencia usando una ventana de tamaño k.
5. Obtener el k-mer de la posición actual.
6. Contar cuántas letras G o C tiene ese k-mer.
7. Mostrar el k-mer actual junto con su valor GC.
8. Comparar ese valor con el mejor valor guardado.
9. Si el k-mer actual tiene mayor contenido GC, actualizar el mejor resultado.
10. Mostrar el mensaje Best so far con el mejor k-mer registrado hasta ese momento.
11. Al final, mostrar el mejor k-mer, su posición y su contenido GC.

<br>


### 6. Formato esperado de la primera salida 

seq = ATGCG
k = 3

```

Posición 0 → ATG
Posición 1 → TGC
Posición 2 → GCG

```

**Formato esperado de la segunda salida**

```
kmer=ATG GC=1
Best so far → ATG (GC=1)

kmer=TGC GC=2
Best so far → TGC (GC=2)

kmer=GCG GC=3
Best so far → GCG (GC=3)

Final best k-mer: GCG
Position: 2
GC count: 3
```

**Formato esperado de la tercera salida**

```
ATGCG
^^^  kmer=ATG GC=1
Best so far → ATG (GC=1)

ATGCG
 ^^^  kmer=TGC GC=2
Best so far → TGC (GC=2)

ATGCG
  ^^^  kmer=GCG GC=3
Best so far → GCG (GC=3)

Final best k-mer: GCG
Position: 2
GC count: 3
```