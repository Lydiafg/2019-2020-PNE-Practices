from Seq1 import Seq
import socket
import termcolor

seq_list = ["ACCGTGC", "TCGGAC", "GCATTGCA", "CAGGTCA", "CATTGTCGAGTGTGGCA"]


def get_command(num):
    return seq_list[num]


def info_command(seq):
    real_seq = Seq(seq)
    length = real_seq.len()
    count_A = real_seq.count_base("A")
    count_C = real_seq.count_base("C")
    count_G = real_seq.count_base("G")
    count_T = real_seq.count_base("T")
    per_A = 100 * (count_A / length)
    per_C = 100 * (count_C / length)
    per_G = 100 * (count_G / length)
    per_T = 100 * (count_T / length)
    response_info = f"""Total length {real_seq}: {length}
                     A : {count_A} ({per_A} %)
                     C : {count_C} ({per_C} %)
                     G : {count_G} ({per_G} %)
                     T : {count_T} ({per_T} %)"""
    return response_info


def comp_command(seq):
    real_seq = Seq(seq)
    complement_seq = real_seq.complement()
    return complement_seq


def rev_command(seq):
    real_seq = Seq(seq)
    reverse_seq = real_seq.reverse()
    return reverse_seq


def gene_command(seq):
    folder = "../Session4/"
    file = seq
    format_ = ".txt"
    filename = Seq().read_fasta(folder + file + format_)
    return str(filename)


PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")


while True:

    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()

        exit()

    else:
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)

        msg = msg_raw.decode()

        print(f"Message received: {msg}")

        # ------ Process the command

        # -- Remove the \n
        lines = msg.split("\n")
        line0 = lines[0].strip()

        # -- Separate the line into command and argument

        # -- Eliminate the blank spaces(then we have the message without elements we do not need --> command + argument)
        real_msg = line0.split(' ')

        # -- The first element is the command
        command = real_msg[0]

        # -- Get the first argument (which is the second element)
        try:
            argument = real_msg[1]
        except IndexError:
            argument = " "

        # -- Response message
        response = ""

        if command == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!"
        elif command == "GET":
            termcolor.cprint("GET", 'green')
            response = get_command(int(argument))
        elif command == "INFO":
            termcolor.cprint("INFO", 'green')
            response = info_command(argument)
        elif command == "COMP":
            termcolor.cprint("COMP", 'green')
            response = comp_command(argument)
        elif command == "REV":
            termcolor.cprint("REV", 'green')
            response = rev_command(argument)
        elif command == "GENE":
            termcolor.cprint("GENE", 'green')
            response = gene_command(argument)
        else:
            termcolor.cprint("Unknown command!!!", 'red')
            response = "Unkwnown command"

        print(response)
        cs.send(response.encode())
        cs.close()