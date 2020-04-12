from Seq1 import Seq

folder = "../Session4/"
format_ = ".txt"
filename = "U5"


print("-----| Practice 1, Exercise 3 |------")
print()

s1 = Seq()
s1.read_fasta(folder + filename + format_)

print(f"Sequence {filename + format_}: (Length: {s1.len()})", f"{s1}")
print(f" Bases : {s1.count()}")
print(f"Rev: {s1.reverse()}")
print(f"Comp: {s1.complement()}")