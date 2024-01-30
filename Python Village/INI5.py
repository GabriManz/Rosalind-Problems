f = open('Database/rosalind_ini5.txt', 'r')
lines = f.readlines()
output = []
for linenumber, line in enumerate(lines):
    if linenumber % 2:
        output.append(line)

outfile = open('Database/rosalind_out_ini5.txt', 'w')
outfile.write(''.join(output))

f.close()
outfile.close()