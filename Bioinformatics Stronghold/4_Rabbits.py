with open('Database/rosalind_fib.txt', 'r') as infile:
    data = infile.readline().split(' ')

month = int(data[0])
offsprings = int(data[1])

parent, child = 1, 1

for i in range(month - 1):
    child, parent = parent, parent + (child * offsprings)

print(f'month = {month}, offsprings = {offsprings}, child = {child}')