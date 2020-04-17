from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

print("* Testing PING...")
c.debug_talk("PING")
print()

print("* Testing GET...")
c.debug_talk("GET 0")
c.debug_talk("GET 1")
c.debug_talk("GET 2")
c.debug_talk("GET 3")
c.debug_talk("GET 4")
print()

print("INFO...")
print(f"Sequence: {c.debug_talk('GET 0')}")
c.debug_talk(f"INFO {c.debug_talk('GET 0')}")
print()

print("COMP...")
print(f"Sequence: {c.debug_talk('GET 0')}")
c.debug_talk(f"COMP {c.debug_talk('GET 0')}")
print()

print("REV...")
print(f"Sequence: {c.debug_talk('GET 0')}")
c.debug_talk(f"REV {c.debug_talk('GET 0')}")
print()

print("GENE...")
c.debug_talk("GENE U5")
print()
c.debug_talk("GENE ADA")
print()
c.debug_talk("GENE FRAT1")
print()
c.debug_talk("GENE FXN")
print()
c.debug_talk("GENE RNU6-269P")
print()