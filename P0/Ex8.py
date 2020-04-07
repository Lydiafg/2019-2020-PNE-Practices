from Seq0 import *

folder = "../Session-04/"
format_ = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ['A', 'T', 'C', 'G']

print("----- Exercise 8 ------")

for gene in genes:
    sequence = seq_read_fasta(folder + gene + format_)
    values_dict = seq_count(sequence)
    values_list = list(values_dict.values())

    m = max(values_list)
    print(f"Gene {gene} : Most frequent Base = {bases[values_list.index(m)]}")