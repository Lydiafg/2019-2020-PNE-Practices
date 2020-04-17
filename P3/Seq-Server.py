
import socket
import termcolor

PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

seq0 = "ACCGTGC"
seq1 = "TCGGAC"
seq2 = "GCATTGCA"
seq3 = "CAGGTCA"
seq4 = "CATTGTCGAGTGTGGCA"
seq_list = [seq0, seq1, seq2, seq3, seq4]
get_strings = ["GET 0", "GET 1", "GET 2", "GET 3", "GET 4"]


while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        if msg == "PING":
            termcolor.cprint(f"{msg} command!", "green")
            response = "OK!"
            cs.send(response.encode())
            cs.close()

        elif msg in get_strings:
            print("GET")
            if msg == "GET 0":
                response = seq_list[0]
                print(response)
                cs.send(response.encode())
                cs.close()
            elif msg == "GET 1":
                response = seq_list[1]
                print(response)
                cs.send(response.encode())
                cs.close()
            elif msg == "GET 2":
                response = seq_list[2]
                print(response)
                cs.send(response.encode())
                cs.close()
            elif msg == "GET 3":
                response = seq_list[3]
                print(response)
                cs.send(response.encode())
                cs.close()
            elif msg == "GET 4":
                response = seq_list[4]
                print(response)
                cs.send(response.encode())
                cs.close()

        else:
            # -- Print the received message
            print(f"Message received: {msg}")

            # -- Send a response message to the client
            response = "HELLO. I am the Happy Server :-)\n"

            # -- The message has to be encoded into bytes
            cs.send(response.encode())

            # -- Close the data socket
            cs.close()