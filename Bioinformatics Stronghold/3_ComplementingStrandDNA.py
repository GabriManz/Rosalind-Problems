with open('Database/rosalind_revc.txt', 'r') as infile:
    dna = list(infile.read().rstrip())

reverse_dna = dna[::-1]

reverse_complement = []

replace = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

for i in reverse_dna:
    reverse_complement.append(replace[i])

with open('Database/rosalind_revc_outfile.txt', 'w') as outfile:
    outfile.write( ''.join(reverse_complement))

