from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.52"
PORT1 = 8080
PORT2 = 8081
folder = "../Session4/"
filename = "FRAT1"
format_ = ".txt"

complete_file = str(Seq().read_fasta(folder + filename + format_))

c1 = Client(IP, PORT1)
print(c1)

c2 = Client(IP, PORT2)
print(c2)

print("Sending a message to the server...")
c1.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases ...")
c2.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases ...")

length = 10
odd_numbers = [1, 3, 5, 7, 9]

for i in range(10):
    fragment = complete_file[i*length:(i+1)*length]
    print(f"Fragment {i+1} : {fragment}")
    if i+1 == odd_numbers:
        c1.talk(f"Fragment {i+1} : {fragment}")
    else:
        c2.talk(f"Fragment {i + 1} : {fragment}")