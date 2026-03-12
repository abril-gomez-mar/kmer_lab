# Generar k-mers a partir de una secuencia de DNA

# 1. Leer la secuencia de DNA.
seq = input('DNA: ').upper()

# 2. Leer el valor de k.
k = int(input(f'Introduzca el valor de k: '))

# 3. Revisar, antes de realizar el análisis, que la secuencia no esté vacía.
if not seq:
    print(f'No se introdujo ninguna secuencia. Intente de nuevo.')
    print(f'No puede mostrarse ninguna posición.') 

else:    

# 4.  Validar que k no rebase la longitud de la secuencia.
 if len(seq) < k: 
    print(f'Su secuencia es demasiado corta, dado el valor seleccionado de k.')
    print(f'No puede mostrarse ninguna posición.')

   
# 5. Recorrer la secuencia con una ventana de tamaño k.
 else:
    
    for i in range(len(seq) - k + 1):

    # 6. Extraer el k-mer de la posición actual.
     kmer = seq[i:i+k]
     gc_count = kmer.count('G') + kmer.count('C')
     
     # 7. Determinar, con base en el conteo de GC, cuál es el mejor k-mer encontrado hasta el momento.
     # Las variables best_kmer, best_gc_count y posicion se inicializan con los datos del primer k-mer.
     # Dichas variables solo se actualizan si el contenido de GC de futuros kmers es mayor que el valor actual de best_gc_count.

     if i == 0:
        best_kmer = kmer
        best_gc_count = gc_count
        posicion = 0

     else:
        if gc_count > best_gc_count:
            best_kmer = kmer
            best_gc_count = gc_count 
            posicion = i

    # 8. Mostrar el k-mer.
     print(f'kmer={kmer} GC={gc_count}')
     print(f'Best so far → {best_kmer} (GC={best_gc_count})\n')

    # 9. Al finalizar el recorrido, mostrar el mejor k-mer encontrado, su posición y su conteo de GC.
    print(f'Final best k-mer: {best_kmer}')
    print(f'Position: {posicion}')
    print(f'GC count: {best_gc_count}')