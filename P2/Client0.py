import socket
import termcolor
class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        return

    @staticmethod
    def ping():
        print("OK")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating the socket
        s.connect((self.ip, self.port))  # connecting to the ip and port
        s.send(str.encode(msg))  # sending the message
        response = s.recv(2048).decode("utf-8")  # receiving other message
        s.close()  # closing the socket
        return response

    def debug_talk(self, to_server):
        from_server = self.talk(to_server)
        print("To server: ", end="")
        termcolor.cprint(to_server, "blue")
        print("From server: ", end="")
        termcolor.cprint(from_server, "yellow")
        return from_server
