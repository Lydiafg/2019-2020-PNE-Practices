from Seq_0 import*

folder = "../Session-04/"
format_ = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("----- Exercise 4 ------")


for gene in genes:
    sequence = seq_read_fasta(folder + gene + format_)
    print()
    print(f"Gene {gene}:")
    for base in bases:
        print(f"  {base}: {seq_count_base(sequence)}")