from Seq0 import*

folder = "../Session4/"
format_ = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]

print("---- Exercise 3 ----")

for gene in genes:
    sequence = seq_read_fasta(folder + gene + format_)
    print(f"Gene {gene} : Lenght = {seq_len(sequence)}")