from Bio import Entrez
from Bio import SeqIO

with open('Database/rosalind_frmt.txt', 'r') as infile:
    data = infile.read().strip().split()

Entrez.email = 'gabrielmanzanoreche@gmail.com'
records = []

for genbank_id in data:
    handle = Entrez.efetch(db='nucleotide', id=genbank_id, rettype='fasta')
    record = SeqIO.read(handle, 'fasta')
    records.append(record)
    handle.close()

# Find the record with the shortest sequence
shortest_record = min(records, key=lambda x: len(x.seq))

# Print the result
print(f'>{shortest_record.description}\n{shortest_record.seq}')
