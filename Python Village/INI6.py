f = open('Database/rosalind_ini6.txt', 'r')
lines = f.readlines()
words = ' '.join(lines).split() 

word_frequency = {} 
output = []

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1 
    else:
        word_frequency[word] = 1

outfile = open('Database/rosalind_out_ini6.txt', 'w')

for word in word_frequency:
    line = ' '.join([word, str(word_frequency[word])])
    output.append(line)

outfile.write('\n'.join(output))
outfile.close()
