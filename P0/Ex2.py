from Seq_0 import *

folder = "../Session4/"
filename = "U5.txt"
file = folder + filename

print("---- Exercise 2 ----")
print("DNA file: ", filename)
sequence = seq_read_fasta(file)
print("The first 20 bases are: ")
print(sequence[:20])