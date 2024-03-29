#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

with open('Database/rosalind_dna.txt', 'r') as infile:
    dna = infile.read().rstrip()

nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in dna:
    nucleotides[i] += 1

for count in nucleotides.values():
    print(count, end = ' ')

print('\n')