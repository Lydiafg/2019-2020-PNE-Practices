from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
sequences = [s1, s2, s3]

print("-----| Practice 1, Exercise 8 |------")
print()

for i, s in enumerate(sequences):
    print(f"Sequence {i}: (Length: {s.len()})", f"{s}")
    print(f" Bases : {s.count()}")
    print(f"Rev: {s.reverse()}")
    print(f"Comp: {s.complement()}")