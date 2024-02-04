with open('Database/rosalind_prot.txt', 'r') as infile:
    data = infile.readline().rstrip()

codon = { 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 
'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 
'UAG': 'STOP', 'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W', 
'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 
'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 
'CGU': 'R', 'CGC': 'R', 'CGA':  'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 
'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 
'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 
'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 
'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

protein = ''
i = 0

while i in range(0, len(data), 3):
    code = data[i:i+3]
    if code != 'UAA' and code != 'UAG' and code != 'UGA':
        protein += codon[code]
    else: 
        break

with open('Database/rosalind_prot_outfile.txt', 'w') as outfile:
    outfile.write(''.join(protein))
