with open('Database/rosalind_iprb.txt', 'r') as infile:
    data = infile.readline().split(' ')

k = int(data[0])
m = int(data[1])
n = int(data[2])
p = k + m + n

probability = (
    1 * ((k/p) * ((k - 1) / (p - 1))) +
    1 * ((k / p) * (m / (p - 1)) + (m / p) * (k / (p - 1))) +
    1 * ((k / p) * (n / (p - 1)) + (n / p) * (k / (p - 1))) +
    0.75 * (m / p) * ((m - 1) / (p - 1)) +
    0.5 * ((m / p) * (n / (p - 1)) + (n / p) * (m / (p - 1))) +
    0 * (n / p) * ((n - 1) / (p - 1))
)

print(probability)
