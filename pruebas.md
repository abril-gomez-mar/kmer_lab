# Casos de prueba

## **Primer programa: obtención de k-mers.**

### Caso normal

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: ATGCG | ATG TGC GCG | 
| k: 3 | Posición 0 → ATG Posición 1 → TGC Posición 2 → GCG |

Este caso contempla que se introduce una secuencia de la cual pueden extraerse numerosos kmers.

 - Resultados
  ```
ATG
Posición 0 -> ATG
TGC
Posición 1 -> TGC
GCG
Posición 2 -> GCG
  ```

 - ¿Coincide con la salida esperada? Sí.

### Primer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: ATG | ATG |
| k: 3 | Posición 0 → ATG |

Este caso prevé que se introduce una secuencia asociada a un solo kmer.

 - Resultados
  ```
ATG
Posición 0 -> ATG
  ```

 - ¿Coincide con la salida esperada? Sí.

### Segundo caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: AT | Su secuencia es demasiado corta, dado el valor seleccionado de k. |
| k: 3 | No puede mostrarse ninguna posición. | 

Este caso asume que se escogió una secuencia de la cual no puede extraerse ningún kmer, dado el valor seleccionado para k.

 - Resultados
  ```
Su secuencia es demasiado corta, dado el valor seleccionado de k.
No puede mostrarse ninguna posición.
  ```

 - ¿Coincide con la salida esperada? Sí.

### Tercer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: | No se introdujo ninguna secuencia. Intente de nuevo. |
| k: 3 | No puede mostrarse ninguna posición. |

Este caso presume que el usuario no introdujo ninguna secuencia, así que no puede aislarse ningún kmer.

 - Resultados
  ```
No se introdujo ninguna secuencia. Intente de nuevo.
No puede mostrarse ninguna posición.
  ```

 - ¿Coincide con la salida esperada? Sí.

<br>

## **Segundo programa: mejor kmer por contenido de GC**

### Caso normal

Entradas
DNA: ATGCG
k: 3

Este caso contempla que se introduce una secuencia de la cual pueden aislarse numerosos kmers.

Salidas
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


 - Resultados
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

 - ¿Coincide con la salida esperada? Sí.

### Primer caso límite

Entradas
DNA: ATG
k: 3

Este caso se presentaría si se introduce una secuencia asociada a un solo kmer.

Salidas
```
kmer=ATG GC=1
Best so far → ATG (GC=1)

Final best k-mer: ATG
Position: 0
GC count: 1
```

 - Resultados
  ```
kmer=ATG GC=1
Best so far → ATG (GC=1)

Final best k-mer: ATG
Position: 0
GC count: 1
  ```

 - ¿Coincide con la salida esperada? Sí.

### Segundo caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: AT  | Su secuencia es demasiado corta, dado el valor seleccionado de k. |
| k: 3 | No puede mostrarse ninguna posición. | 

Este caso asume que se escogió una secuencia de la cual no puede extraerse ningún kmer, considerando el valor seleccionado para k.

 - Resultados
  ```
Su secuencia es demasiado corta, dado el valor seleccionado de k.
No puede mostrarse ninguna posición.
  ```

 - ¿Coincide con la salida esperada? Sí.

### Tercer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: | No se introdujo ninguna secuencia. Intente de nuevo. |
| k:3 | No puede mostrarse ninguna posición. |

Este caso presume que el usuario no introdujo ninguna secuencia, así que no puede identificarse ningún kmer.

 - Resultados
  ```
No se introdujo ninguna secuencia. Intente de nuevo.
No puede mostrarse ninguna posición.
  ```

 - ¿Coincide con la salida esperada? Sí.

<br>

## **Tercer programa: visualización de ventana deslizante**

### Caso normal

Entradas
DNA: ATGCG
k: 3

Este caso contempla que se introduce una secuencia de la cual pueden aislarse numerosos kmers.

Salidas
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


 - Resultados
  ```
ATGCG
^^^ kmer=ATG GC=1
Best so far → ATG GC=1

ATGCG
 ^^^ kmer=TGC GC=2
Best so far → TGC GC=2

ATGCG
  ^^^ kmer=GCG GC=3
Best so far → GCG GC=3

Final best k-mer: GCG
Position: 2
GC count: 3

  ```

 - ¿Coincide con la salida esperada? Sí.

 
### Primer caso límite
Entradas
DNA: ATG
k: 3

Este caso se suscitaría si se introduce una secuencia asociada a un solo kmer.

Salidas
```
ATG
^^^  kmer=ATG GC=1
Best so far → ATG (GC=1)

Final best k-mer: ATG
Position: 0
GC count: 1
```

 - Resultados
  ```
ATG
^^^ kmer=ATG GC=1
Best so far → ATG GC=1

Final best k-mer: ATG
Position: 0
GC count: 1
  ```

 - ¿Coincide con la salida esperada? Sí.

### Segundo caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: AT  | Su secuencia es demasiado corta, dado el valor seleccionado de k. |
| k: 3 | No puede mostrarse ninguna posición. | 

Este caso asume que se escogió una secuencia de la cual no puede extraerse ningún kmer, teniendo en mente el valor seleccionado para k.

 - Resultados
  ```
Su secuencia es demasiado corta, dado el valor seleccionado de k.

No puede mostrarse ninguna posición.
  ```

 - ¿Coincide con la salida esperada? Sí.

### Tercer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: | La secuencia está vacía o el valor de k no es válido. Intente de nuevo. |
| k:3 | No puede mostrarse ninguna posición. |

Este caso se manifestaría si el usuario no introduce ninguna secuencia de DNA.

 - Resultados
  ```
La secuencia está vacía o el valor de k no es válido. Intente de nuevo.

No puede mostrarse ninguna posición.
  ```

 - ¿Coincide con la salida esperada? Sí.
