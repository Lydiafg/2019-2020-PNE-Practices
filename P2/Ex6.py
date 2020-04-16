from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.52"
PORT = 8080
folder = "../Session4/"
filename = "FRAT1"
format_ = ".txt"

complete_file = str(Seq().read_fasta(folder + filename + format_))

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases ...")
c.talk(complete_file)

length = 10

for i in range(5):
    fragment = complete_file[i*length:(i+1)*length]
    print(f"Fragment {i+1} : {fragment}")
    c.talk(f"Fragment {i+1} : {fragment}")
