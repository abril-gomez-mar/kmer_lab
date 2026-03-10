# Generar k-mers a partir de una secuencia de DNA

# 1. Leer la secuencia de DNA
seq = input('DNA: ').upper()

# 2. Leer el valor de k
k = int(input(f'Introduzca el valor de k: '))

# 3. Recorrer la secuencia con una ventana de tamaño k
for i in range(len(seq) - k + 1):

    # 4. Extraer el k-mer de la posición actual
    kmer = seq[i:i+k]

    # 5. Mostrar el k-mer
    print(kmer)
    print(f'Posición {i} -> {kmer}')



    #Falta poner validaciones al comienzo del programa. 