# transcribing dna to rna
# replace every 'T' by a 'U'

with open('Database/rosalind_rna.txt', 'r') as infile:
    dna = list(infile.read().rstrip())

for i in range(len(dna)):
    if dna[i] == 'T':
        dna[i] = 'U'

with open('Database/rosalin_rna_outfile.txt', 'w') as outfile:
    outfile.write(''.join(dna))