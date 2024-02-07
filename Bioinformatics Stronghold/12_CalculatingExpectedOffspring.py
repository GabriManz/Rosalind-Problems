with open('Database/rosalind_iev.txt', 'r') as infile:
    data = infile.readline().split(' ')

population = {
	'AA-AA': int(data[0]),
    'AA-Aa': int(data[1]),
    'AA-aa': int(data[2]),
    'Aa-Aa': int(data[3]),
    'Aa-aa': int(data[4]),
    'aa-aa': int(data[5])
	}

#The expected number of offspring displaying the dominant phenotype in the next generation
dominance = {'AA-AA': 1, 
             'AA-Aa': 1, 
             'AA-aa': 1, 
             'Aa-Aa': 0.75, 
             'Aa-aa': 0.5, 
             'aa-aa': 0} 

offspring = 0

for i in dominance:
    offspring = offspring + dominance[i]*population[i]

# Every couple has exactly two offspring
offspring = 2 * offspring

print(f'The expected number of offspring displaying the dominant phenotype in the next generation: {offspring}')