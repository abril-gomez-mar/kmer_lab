# Casos de prueba

**Primer programa: obtención de k-mers.**

## Caso normal

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: ATGCG | ATG TGC GCG | 
| k: 3 | Posición 0 → ATG Posición 1 → TGC Posición 2 → GCG |

 - Resultados
  ```
ATG
Posición 0 -> ATG
TGC
Posición 1 -> TGC
GCG
Posición 2 -> GCG
  ```

 -¿Coincide con la salida esperada? Sí.

## Primer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: ATG | ATG |
| k: 3 | Posición 0 → ATG |

 - Resultados
  ```
ATG
Posición 0 -> ATG
  ```

 -¿Coincide con la salida esperada? Sí.

## Segundo caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: AT | Su secuencia es demasiado corta, dado el valor seleccionado de k. |
| k: 3 | No puede mostrarse ninguna posición. | 

 - Resultados
  ```
Su secuencia es demasiado corta, dado el valor seleccionado de k.
No puede mostrarse ninguna posición.
  ```

 -¿Coincide con la salida esperada? Sí.

## Tercer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: | No se introdujo ninguna secuencia. Intente de nuevo. |
| k: 3 | No puede mostrarse ninguna posición. |

 - Resultados
  ```
No se introdujo ninguna secuencia. Intente de nuevo.
No puede mostrarse ninguna posición.
  ```

 -¿Coincide con la salida esperada? Sí.


**Segundo programa: mejor kmer por contenido de GC**

## Caso normal

Entradas
DNA: ATGCG
k: 3

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

 -¿Coincide con la salida esperada? Sí.

## Primer caso límite

Entradas
DNA: ATG
k: 3

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

 -¿Coincide con la salida esperada? Sí.

## Segundo caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: AT  | Su secuencia es demasiado corta, dado el valor seleccionado de k. |
| k: 3 | No puede mostrarse ninguna posición. | 

 - Resultados
  ```
Su secuencia es demasiado corta, dado el valor seleccionado de k.
No puede mostrarse ninguna posición.
  ```

 -¿Coincide con la salida esperada? Sí.

## Tercer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: | No se introdujo ninguna secuencia. Intente de nuevo. |
| k:3 | No puede mostrarse ninguna posición. |

 - Resultados
  ```
No se introdujo ninguna secuencia. Intente de nuevo.
No puede mostrarse ninguna posición.
  ```

 -¿Coincide con la salida esperada? Sí.


**Tercer programa: visualización de ventana deslizante**

## Caso normal

Entradas
DNA: ATGCG
k: 3

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
^^^  Best so far → ATG (GC=1)

ATGCG
 ^^^  Best so far → TGC (GC=2)

ATGCG
  ^^^  Best so far → GCG (GC=3)

Final best k-mer: GCG
Position: 2
GC count: 3

  ```

 -¿Coincide con la salida esperada? Sí.

 
## Primer caso límite
Entradas
DNA: ATG
k: 3

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
^^^  Best so far → ATG (GC=1)

Final best k-mer: ATG
Position: 0
GC count: 1
  ```

 -¿Coincide con la salida esperada? Sí.

## Segundo caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: AT  | Su secuencia es demasiado corta, dado el valor seleccionado de k. |
| k: 3 | No puede mostrarse ninguna posición. | 

 - Resultados
  ```
Su secuencia es demasiado corta, dado el valor seleccionado de k.

No puede mostrarse ninguna posición.
  ```

 -¿Coincide con la salida esperada? Sí.

## Tercer caso límite

|  Entrada |  Salida esperada | 
|---|---|
|  DNA: | No se introdujo ninguna secuencia. Intente de nuevo. |
| k:3 | No puede mostrarse ninguna posición. |

 - Resultados
  ```
No se introdujo ninguna secuencia. Intente de nuevo.

No puede mostrarse ninguna posición.
  ```

 -¿Coincide con la salida esperada? Sí.