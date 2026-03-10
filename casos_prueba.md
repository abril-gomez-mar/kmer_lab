# Casos de prueba

Programa: Obtención de k-mer.

""
""
""
""
Casos de prueba manuales

## Caso normal
|  Entrada |  Salida esperada | 
|---|---|
|  DNA: ATGCG | ATG TGC GCG | 
| k:3 | Posición 0 → ATG Posición 1 → TGC Posición 2 → GCG |

## Primer caso límite
|  Entrada |  Salida esperada | 
|---|---|
|  DNA: ATG | ATG |
| k:3 | Posición 0 → ATG |

## Segundo caso límite
|  Entrada |  Salida esperada | 
|---|---|
|  DNA: AT k:3 | Su secuencia es demasiado corta, dado el valor seleccionado de k |
| k:3 | No puede mostrarse ninguna posición | 

## Tercer caso límite
|  Entrada |  Salida esperada | 
|---|---|
|  DNA: | "No se introdujo ninguna secuencia. Intente de nuevo" |
| k:3 | No puede mostrarse ninguna posición |


