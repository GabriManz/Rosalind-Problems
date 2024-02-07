from Bio.Seq import Seq

with open('Database/rosalind_ini.txt', 'r') as infile:
    data = Seq(infile.read().strip())

A = data.count('A')
C = data.count('C')
G = data.count('G')
T = data.count('T')

print(f'{A} {C} {G} {T}')
