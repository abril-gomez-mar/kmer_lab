# Programa de k-mers.

## 1. Descripción del problema

Al dividir una secuencia de ADN en fragmentos de cierta longitud k, surgen los kmers. 
Dado que las cadenas de material genético tienen bastantes pares de bases, puede ser complicado visualizar los kmers, compararlos mediante un criterio esencial (el contenido de GC), y saber cuál obtuvo la puntuación más elevada.

<br>

## 2. Objetivo del software

Obtener, dada una secuencia y un valor de k proporcionados por el usuario, los kmers de una cadena de ADN.

<br>

## 3. Requisitos funcionales (de la versión final del programa)

-Leer una secuencia de DNA.
-Leer el valor de k.
-Recorrer la secuencia.
-Generar todos los k-mers de longitud k.
-Mostrar cada k-mer en pantalla.
- Calcular cuántos nucleótidos G o C tiene cada k-mer.
- Comparar el valor GC de cada k-mer con el mejor encontrado hasta el momento.
- Guardar el mejor k-mer.
- Guardar la posición donde aparece.
- Mostrar al final el mejor resultado encontrado.
-Mostrar la secuencia completa en cada iteración.
-Mostrar una línea visual que indique la posición actual de la ventana de tamaño k.
-Alinear esa visualización con el k-mer que se está evaluando.

<br>

## 4. Requisitos no funcionales
- El programa debe aceptar secuencias en mayúsculas o minúsculas.
- La secuencia debe convertirse a mayúsculas.
- El código debe ser legible y seguir convenciones básicas de estilo, según PEP-8.

<br> 

## 5. Supuestos y limitaciones
- Solo puede procesarse una cadena de ADN a la vez, usando un valor específico de k.
- La cadena de ADN no debe contener espacios.

<br>

## 6. Análisis del problema
Para saber cuáles son los kmers de una secuencia, es menester resguardar los inputs y luego leer fragmentos de la cadena mediante un ciclo for. 
Por cada iteración, se aislará un kmer y su contenido de GC será calculado. Este parámetro, al igual que la posición y secuencia del kmer, deben resguardarse para el primer kmer.
Aquel total de GC será equivalente al mejor valor provisional de guanina y citosina. El valor de esta última variable y los valores de los otros dos parámetros citados podrán actualizarse conforme se extraigan más kmers y se determine su contenido de C y G.

Para que el usuario vea cómo va avanzando el programa, debe emplearse una ventana deslizante que señalice cuáles nucleótidos de la secuencia original constituyen el kmer actual, así como el valor correspondiente de GC.
Asimismo, es necesario puntualizar cuál, hasta ahora, ha sido el kmer con el mayor contenido de GC. Al final, debe indicarse cuál fue el kmer con mayor presencia de GC.


<br>

## 7. Diseño de la solución

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

