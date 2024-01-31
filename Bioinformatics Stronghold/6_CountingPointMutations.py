with open('Database/rosalind_hamm.txt', 'r') as infile:
    data = infile.read().splitlines()

sequence_one = data[0]
sequence_two = data[1]
hamming_distance = 0

for i in range(len(sequence_one)):
    if sequence_one[i] != sequence_two[i]:
        hamming_distance += 1

print(f'Hamming distance: {hamming_distance}')
