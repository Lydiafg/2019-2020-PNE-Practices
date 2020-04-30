import http.client
import json
import termcolor
from Seq1 import Seq

GENES = {
     'FRAT1': 'ENSG00000165879',
     'SRCAP': 'ENSG00000080603',
     'ADA': 'ENSG00000196839',
     'FXN': 'ENSG00000165060',
     'RNU6_269P': 'ENSG00000212379',
     'MIR633': 'ENSG00000207552',
     'TTTY4C': 'ENSG00000228296',
     'FGFR3': 'ENSG00000068078',
     'KDR': 'ENSG00000128052',
     'ANK2': 'ENSG00000145362',
 }

SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
PARAMETERS = "?content-type=application/json"




# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    for gene in GENES:
        REQ_LINE = ENDPOINT + GENES[gene] + PARAMETERS
        URL = SERVER + REQ_LINE

        print()
        print(f"Server: {SERVER}")
        print(f"URL : {URL}")

        conn.request("GET", REQ_LINE)
        r1 = conn.getresponse()

        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # -- Read the response's body
        data1 = r1.read().decode()

        # -- Create a variable with the data,
        # -- form the JSON received
        gene_info = json.loads(data1)

        print()
        termcolor.cprint("Gene :", "green", end=" ")
        print(f"{gene}")
        termcolor.cprint("Description :", "green", end=" ")
        print(f"{gene_info['desc']}")

        sequence = Seq(gene_info['seq'])

        termcolor.cprint("Total length: ", "green", end=" ")
        print(f"{sequence.len()}")

        bases = ['A', 'C', 'G', 'T']

        for base in bases:
            termcolor.cprint(base, "blue", end=" ")
            print(f": {sequence.count_base(base)}", end=" ")
            percentage_base = "{:.1f}".format(sequence.count_base(base) / sequence.len() * 100)
            print(f"({percentage_base} %)")

        max = 0
        max_base = ""
        for base in bases:
            if sequence.count_base(base) > int(max):
                max = sequence.count_base(base)
                max_base = base

        print("Most frequent base: ", {max_base})

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
