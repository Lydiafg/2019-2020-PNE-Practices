from Client0 import Client

IP = "192.168.1.52"
PORT = 8080

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")

msg_num = 0

for i in range(5):
    msg_num += 1
    c.debug_talk(f"Message {msg_num}")
