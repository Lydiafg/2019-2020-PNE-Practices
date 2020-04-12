from Seq1 import Seq

folder = "../Session4/"
format_ = ".txt"
filenames = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ['A', 'T', 'C', 'G']


print("-----| Practice 1, Exercise 10 |------")
print()

for filename in filenames:
    s1 = Seq().read_fasta(folder + filename + format_)
    values_dict = s1.count()
    values_list = list(values_dict.values())
    maximum = max(values_list)
    print(f"Gene {filename}: Most frequent Base: {bases[values_list.index(maximum)]}")
