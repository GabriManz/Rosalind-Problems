with open('Database/rosalind_subs.txt', 'r') as infile:
    data = infile.readlines()

dna = data[0].rstrip()
motif = data[1].rstrip()

index = []
for i in range(len(dna) - len(motif) + 1):  # Ajuste en el rango
    test = dna[i:i+len(motif)]
    if test == motif:
        index.append(str(i+1))  # Convertir el índice a cadena

with open('Database/rosalind_subs_outfile.txt', 'w') as outfile:
    outfile.write(' '.join(index))


#NOT FINISHED
