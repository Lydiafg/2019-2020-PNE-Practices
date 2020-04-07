from Seq0 import *

folder = "../Session-04/"
format_ = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("----- Exercise 7 ------")

gene = genes[0]
print(f"Gene {gene}:")
sequence = seq_read_fasta(folder + genes[0] + format_)[:20]
complement = seq_complement(sequence)
print(f"Frag: {sequence}")
print(f"Comp: {complement}")