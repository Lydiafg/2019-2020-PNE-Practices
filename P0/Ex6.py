from Seq_0 import *

folder = "../Session-04/"
format_ = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("----- Exercise 6 ------")

gene = genes[0]

print(f"Gene {gene}:")
sequence = seq_read_fasta(folder + genes[0] + format_)[:20]
reverse = seq_reverse(sequence)
print(f"Fragment : {sequence}")
print(f"Reverse sequence : {reverse}")