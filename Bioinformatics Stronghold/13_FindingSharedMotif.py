with open('Database/rosalind_.txt', 'r') as infile:
    data = infile.readlines()

sequence = {}
label = None

for line in data:
    line = line.rstrip()
    if line.startswith('>'):
        label = line
        sequence[label] = ""
    else:
        sequence[label] += line

strings = list(sequence.values())

