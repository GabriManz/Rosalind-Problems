with open('Database/rosalind_fibd.txt', 'r') as infile:
    data = infile.readline().split(' ')

month = int(data[0])
survival_time = int(data[1])

bunnies = [1, 1]
months = 2

#Fn = Fn-1 + Fn-2 - Fn-(m+1)
while months < month:
    if months < survival_time:
        bunnies.append(bunnies[-2] + bunnies[-1])
    elif months == survival_time or months == survival_time + 1:
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)
    else:
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(survival_time + 1)])
    months += 1

print(bunnies[-1])