from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print("-----| Practice 1, Exercise 3 |------")
print()

print(f"Sequence 1: (Length: {s1.len()})", f"{s1}")
for base in ['A', 'C', 'T', 'G']:
    print(f"  {base}: {s1.count_base(base)}", end=", ")
print()

print(f"Sequence 2: (Length: {s2.len()})", f"{s2}")
for base in ['A', 'C', 'T', 'G']:
    print(f"  {base}: {s2.count_base(base)}", end=", ")
print()

print(f"Sequence 3: (Length: {s3.len()})", f"{s3}")
for base in ['A', 'C', 'T', 'G']:
    print(f"  {base}: {s3.count_base(base)}", end=", ")
print()
