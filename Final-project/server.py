import http.server
import http.client
import socketserver
import json
import termcolor
from pathlib import Path

# description of the URL which we connect when taking info from API rest
SERVER = 'rest.ensembl.org'
ENDPOINT = ["/info/species", "/info/assembly/"]
PARAMETERS = "?content-type=application/json"

# port of the server we are creating
PORT = 8080

# This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    # this will be called when the client wants the GET method
    def do_GET(self):

        # this writes the request line of the client in the server console (in green)
        termcolor.cprint(self.requestline, 'green')

        # with this we separate the arguments in the request line to analyze it
        req_line = self.requestline.split(' ')
        path = req_line[1]

        contents = ""
        status = 0

        arguments = path.split('?')
        verb = arguments[0]

        # these are the options that the client (by the request line) would select
        # the first three are for presenting the main menu of the python application
        if path == "":
            contents = Path("main.html").read_text()
            status = 200
        elif path == "main.html":
            contents = Path("main.html").read_text()
            status = 200
        elif verb == "/":
            contents = Path('main.html').read_text()
            status = 200

        # this option is called when the client wants to know the list of species in ensembl
        elif verb == "/listSpecies":

            # we connect to the server (API rest ensembl web)  and separate the arguments
            REQ_LINE = ENDPOINT[0] + PARAMETERS
            conn = http.client.HTTPConnection(SERVER)

            pair = arguments[1]
            msg, limit = pair.split("=")
            limit = int(limit)
            try:
                conn.request("GET", REQ_LINE)
            except ConnectionRefusedError:  # this is for if the client cannot connect to the server (ensembl)
                print("ERROR! Cannot connect to the Server")
                exit()

            # we print the status of the request to know if it has worked and decode and read the data from the API rest
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode()
            total_info = json.loads(data1)

            species_info = total_info['species']

            # different situations of the limit
            # if we write a limit in the list
            if limit != "":
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT LIST</title>
                            </head>
                            <body style="background-color: lightblue;">
                                <p>The total number of species in the ensembl is: {len(species_info)}</p>
                                <p>The limit you have selected is: {limit}</p>
                                <p>The name of the species are: </p>
                                <ol>  
                            """
                # the for loop to create the list of species till the limit we have put and include it in the html
                species_list = ""
                for i in range(len(species_info [: int(limit)])):
                    species_list = species_list + "<li>"
                    species_list = species_list + species_info[i]['common_name']
                    species_list = species_list + "</li>"
                species_list = species_list + "</ol></body></html>"
                contents += f"<p>{species_list}</p>"
                contents += "</body></html>"

                status = 200

            # if we don´t write a limit
            elif limit == "":
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT LIST</title>
                            </head>
                            <body style="background-color: lightblue;">
                                <p>The total number of species in the ensembl is: {len(species_info)}</p>
                                <p>The limit you have selected is: {limit}</p>
                                <p>The name of the species are: </p>
                                <ol>  
                            """

                # in this case we write the whole list
                species_list = ""
                for i in range(len(species_info)):
                    species_list = species_list + "<li>"
                    species_list = species_list + species_info[i]['common_name']
                    species_list = species_list + "</li>"
                species_list = species_list + "</ol></body></html>"
                contents += f"<p>{species_list}</p>"
                contents += "</body></html>"

                status = 200

            # if we write one out of range
            elif limit > len(species_info):
                contents = Path("Error.html").read_text()
                status = 404

        # this option is called when the client wants to know the karyotype of a specie in ensembl
        elif verb == "/karyotype":
            pair = arguments[1]
            msg, specie = pair.split("=")

            # we firstly connect to the previous API rest method to know if the specie is in the list of the ones in
            # ensembl
            REQ_LINE_1 = ENDPOINT[0] + PARAMETERS
            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", REQ_LINE_1)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode()
            total_info = json.loads(data1)

            species_info = total_info['species']

            # we generate again the list of species and make options
            species_list = ""
            for i in range(len(species_info)):
                species_list = species_list + "<li>"
                species_list = species_list + species_info[i]['common_name']

            # if is in the list then we connect to the second API rest endpoint to have the karyotype (by the same way)
            if specie in species_list:
                REQ_LINE_2 = ENDPOINT[1] + specie + PARAMETERS
                conn = http.client.HTTPConnection(SERVER)

                try:
                    conn.request("GET", REQ_LINE_2)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")
                data1 = r1.read().decode()
                total_info = json.loads(data1)

                species_karyotype = total_info['karyotype']

                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT KARYOTYPE</title>
                            </head>
                            <body style="background-color: lightblue;">
                                <p>The names of the chromosomes are:</p>
                                <ol>  
                            """
                # we make a list of all the names (or numbers) of the chromosomes in the karyotype
                chromosomes_list = ""
                for i in range(len(species_karyotype)):
                    chromosomes_list = chromosomes_list + "<br>"
                    chromosomes_list = chromosomes_list + species_karyotype[i]
                chromosomes_list = chromosomes_list + "</ol></body></html>"
                contents += f"<p>{chromosomes_list}</p>"
                contents += "</body></html>"

                status = 200

            # if the specie is not in the list of species of ensembl we return the Error.html file
            elif specie not in species_list:
                contents = Path("Error.html").read_text()
                status = 400

        # this option is called when the client wants to know the length of a chromosome of a specie in ensembl
        elif verb == "/chromosomeLength":
            pair = arguments[1]
            pairs = pair.split("&")
            pair_1 = pairs[0]
            pair_2 = pairs[1]
            msg, specie = pair_1.split("=")
            msg, chromo = pair_2.split("=")

            # we firstly connect to the first API rest endpoint to know (as in the previous option) if the specie
            # requested is in the list (we follow the same process)
            REQ_LINE_1 = ENDPOINT[0] + PARAMETERS
            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", REQ_LINE_1)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode()
            total_info = json.loads(data1)

            species_info = total_info['species']

            species_list = ""
            for i in range(len(species_info)):
                species_list = species_list + "<li>"
                species_list = species_list + species_info[i]['common_name']

            # if the specie is in the list we connect to the corresponding API rest endpoint to know the length
            if specie in species_list:
                length = None

                REQ_LINE = ENDPOINT[1] + specie + PARAMETERS
                conn = http.client.HTTPConnection(SERVER)

                try:
                    conn.request("GET", REQ_LINE)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")
                data1 = r1.read().decode()
                total_info = json.loads(data1)

                chromosome_info = total_info['top_level_region']

                # the for loop to know the length corresponding to the chromosome (also with the possibility that the
                # chromosome that we have entered is not in the karyotype (in which case we return the Error.html file))
                for i in chromosome_info:
                    if i["coord_system"] == "chromosome" and i["name"] == chromo:
                        length = i["length"]
                    else:
                        length = None

                # if everything is correct we put in html language the page we want to return
                if length != None:
                    contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>RESULT CHROMOSOME LENGTH</title>
                                </head>
                                <body style="background-color: lightblue;">
                                    <p>The length of the chromosome is: {length}</p>
                                </body>
                                </html> 
                                """
                    status = 200
                elif length == None:
                    contents = Path("Error.html").read_text()
                    status = 404

            # if the specie is not in the list (as in te previous option) we return the Error.html file
            elif specie not in species_list:
                contents = Path("Error.html").read_text()
                status = 404

        # if the request line is not like one of the options above (as we do not have that info) we return the
        # Error.html file
        else:
            contents = Path("Error.html").read_text()
            status = 404

        # this is to generate the response message
        self.send_response(status)

        # this is to convert all of the text written above as contents in html format
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        # this is to send the response message
        self.wfile.write(str.encode(contents))

        return


# this is to set the new handler
Handler = TestHandler

# with this we open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    # we print the port at which this server is
    print("Serving at PORT", PORT)

    # this is the main loop (whenever a new client connects the handler is called)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()