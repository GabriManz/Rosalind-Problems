from Bio import Entrez

with open('Database/rosalind_gbk.txt', 'r') as infile:
    data = infile.readlines()

genus_name = data[0].rstrip()
date_entry = data[1].rstrip()
date_out = data[2].rstrip()

Entrez.email = 'gabrielmanzanoreche@gmail.com'

handle = Entrez.esearch(db="nucleotide", 
                        term='"{}"[Organism] AND ("{}"[Publication Date] : "{}"[Publication Date])'.format(genus_name, date_entry, date_out))

record = Entrez.read(handle)

print(record["Count"])