from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print("-----| Practice 1, Exercise 4 |------")
print()
print(f"Sequence 1: (Length: {s1.len()})", f"{s1}")
print(f"Sequence 2: (Length: {s2.len()})", f"{s2}")
print(f"Sequence 3: (Length: {s3.len()})", f"{s3}")