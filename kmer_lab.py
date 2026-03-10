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

    # 7. Mostrar el k-mer.
     print(kmer)
     print(f'Posición {i} -> {kmer}')

