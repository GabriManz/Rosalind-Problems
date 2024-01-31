def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as infile:
        return [l.strip() for l in infile.readlines()]


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


# Calculate GC Content from FASTA formatted text file:

# Read data from the file (FASTA formatted file)
# Storing File contents in a list
FASTAFile = readFile("Database/rosalind_gc.txt")
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""

# === Clean/Prepare the data 
# Converting FASTA file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = "" #Creating the key of the dictionary
    else:
        FASTADict[FASTALabel] += line #Adding the sequence to the label

# Dictionary with GC content value with the key label
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

# Sort the sequences by GC content from highest to lowest
sorted_results = sorted(RESULTDict.items(), key=lambda x: x[1], reverse=True) #items = (key, value)

# Print the sorted results
for label, gc_content_value in sorted_results:
    print(f'{label[1:]}\n{gc_content_value}\n') #label[1:] to eliminate '>'
