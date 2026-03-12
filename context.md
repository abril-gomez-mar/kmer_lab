# Descripción del proyecto.

### 1. Problema
Obtener todos los kmers de una secuencia de ADN brindada por el usuario. El valor k también es un input.

Ejemplo:

Generar todos los fragmentos consecutivos de longitud k (k-mers) a partir de una secuencia de DNA proporcionada por el usuario.

### 2. Datos de entrada

-Una secuencia de DNA introducida por el usuario
-Un número entero k que representa el tamaño del k-mer

### 3. Requisitos funcionales

-Leer una secuencia de DNA
-Leer el valor de k
-Recorrer la secuencia
-Generar todos los k-mers de longitud k
-Mostrar cada k-mer en pantalla

### 4. Requisitos no funcionales

-El programa debe aceptar secuencias en mayúsculas o minúsculas
la secuencia debe convertirse a mayúsculas
el código debe ser legible y seguir convenciones básicas de estilo, según PEP-8.

### 5. Algoritmo

1. Leer la secuencia de DNA.
2. Leer el valor de k.
3. Recorrer la secuencia desde la posición 0 hasta len(seq) - k.
4. En cada posición, extraer un fragmento de longitud k.
5. Mostrar el k-mer generado.

### 6. Formato esperado de la salida 

seq = ATGCG
k = 3

```txt

Posición 0 → ATG
Posición 1 → TGC
Posición 2 → GCG

```