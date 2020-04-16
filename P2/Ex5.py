from Client0 import Client
from Seq1 import Seq  # se pueden importar funciones de diferentes clases a la vez, no hace falta volver a definirlas

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.52"  # tiene que ser el de mi ordenador
PORT = 8080  # es el mismo pq depende de la apliación
folder = "../Session4/"
filename = "U5"
format_ = ".txt"

complete_file = Seq().read_fasta(folder + filename + format_)  # importamos la función de la class Seq

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
c.debug_talk("Sending U5 Gene to the server...")
c.debug_talk(str(complete_file))  # poner el tipo (str) pq sino no lo reconoce