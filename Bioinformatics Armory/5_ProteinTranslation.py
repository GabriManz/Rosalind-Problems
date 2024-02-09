from Bio import SeqIO
from Bio.Seq import translate

def find_genetic_code_variant(dna_sequence, protein_sequence):
    for i in range(1, 16):  # Assuming there are 15 variants, adjust if needed
        translated_protein = translate(dna_sequence, table=i, to_stop=True)
        if translated_protein == protein_sequence:
            return i  # Return the index of the genetic code variant
    return None  # If no match is found

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for record in SeqIO.parse(infile, 'fastq'):  # Change 'fastq' to your actual format if needed
            dna_sequence = record.seq
            protein_sequence = translate(dna_sequence)
            genetic_code_variant = find_genetic_code_variant(dna_sequence, protein_sequence)
            if genetic_code_variant is not None:
                outfile.write(f">{record.id}\n{genetic_code_variant}\n")

input_file_path = "Database/rosalind_ptra.txt"
output_file_path = "Database/rosalind_ptra_out.txt"

main(input_file_path, output_file_path)
