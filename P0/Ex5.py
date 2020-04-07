from Seq0 import *

folder = "../Session-04/"
format_ = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("----- Exercise 5 ------")

for gene in genes:
    sequence = seq_read_fasta(folder + gene + format_)
    print(f"Gene {gene}: {seq_count(sequence)}")