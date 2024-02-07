from Bio import Entrez

with open('Database/rosalind_ini.txt', 'r') as infile:
    data = infile.read().strip()

Entrez.email = 'gabrielmanzanoreche@gmail.com'

handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')

record = Entrez.read(handle)

record["Count"]