from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.52"  # tiene que ser el de mi ordenador
PORT = 8080  # tiene que ser el mismo que pongamos en el server (identificador del server)

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
c.debug_talk("Message 1---")
c.debug_talk("Testing!!!")