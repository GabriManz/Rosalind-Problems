import numpy as np

with open('Database/rosalind_cons.txt', 'r') as infile:
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
matrix = []

for i in strings:
    matrix.append([j for j in i])

matrix_array = np.array(matrix).reshape(len(matrix), len(matrix[0]))

A = []
C = []
G = []
T = []

for i in range(len(matrix[0])):
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    for j in matrix_array[:, i]:
        if j == "A":
            A_count += 1
        elif j == "C":
            C_count += 1
        elif j == "G":
            G_count += 1
        elif j == "T":
            T_count += 1
    A.append(A_count)
    C.append(C_count)
    G.append(G_count)
    T.append(T_count)

result = {'A': A, 'C': C, 'G': G, 'T': T}


with open('Database/rosalind_cons_outfile.txt', 'w') as outfile:
    for i, j in result.items():
        outfile.write(f"{i}: {' '.join(str(x) for x in j)}\n")


