from Bio import SeqIO

def convert_fastq_to_fasta(input_fastq, output_fasta):
    with open(input_fastq, "r") as fastq_file, open(output_fasta, "w") as fasta_file:
        # Parse the FASTQ records and write corresponding FASTA records
        for record in SeqIO.parse(fastq_file, "fastq"):
            fasta_record = ">{}\n{}".format(record.id, record.seq)
            fasta_file.write(fasta_record + "\n")


input_fastq_file = 'Database/rosalind_tfsq.txt'
output_fasta_file = 'Database/rosalind_tfsq_out.txt'

convert_fastq_to_fasta(input_fastq_file, output_fasta_file)