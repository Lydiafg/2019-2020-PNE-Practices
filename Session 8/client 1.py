import socket

IP = "212.128.253.128"
PORT = 8080
# whith this we are creating the socket in the internet and the thing we arew sending is called a stream
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establishing the connection with the server
s.connect((IP, PORT))

# to send a message to the server (we have to convert it into bytes bc the server can only send in that form)
s.send(str.encode("hello"))

# receive data from the server
msg = s.recv(2000) # this is the maximum value of bytes the client will receive from the server
print("Message from the server: \n")
print(msg.decode("utf-8"))

# close the connection
s.close()