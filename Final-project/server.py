import http.server
import http.client
import socketserver
import json
from Seq1 import Seq
import termcolor
from pathlib import Path

SERVER = 'rest.ensembl.org'
ENDPOINT = ["/info/species", "/info/assembly/"]
PARAMETERS = "?content-type=application/json"

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(' ')
        path = req_line[1]

        contents = ""
        status = 0

        arguments = path.split('?')
        verb = arguments[0]

        if path == "":
            contents = Path("main.html").read_text()
            status = 200
        elif path == "main.html":
            contents = Path("main.html").read_text()
            status = 200
        elif verb == "/":
            contents = Path('main.html').read_text()
            status = 200
        elif verb == "/list_limit":

            REQ_LINE = ENDPOINT[0] + PARAMETERS
            conn = http.client.HTTPConnection(SERVER)

            pair = arguments[1]
            msg, value = pair.split("=")

            if value != "":
                value = int(value)
                try:
                    conn.request("GET", REQ_LINE)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")
                data1 = r1.read().decode()
                total_info = json.loads(data1)

                species_info = total_info['species']

                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT LIST</title>
                            </head>
                            <body style="background-color: lightblue;">
                                <p>The total number of species in the ensembl is: {len(species_info)}</p>
                                <p>The limit you have selected is: {value}</p>
                                <p>The name of the species are: </p>
                                <ol>  
                            """

                species_list = ""
                for i in range(len(species_info [: int(value)])):
                    species_list = species_list + "<li>"
                    species_list = species_list + species_info[i]['common_name']
                    species_list = species_list + "</li>"
                species_list = species_list + "</ol></body></html>"
                contents += f"<p>{species_list}</p>"
                contents += "</body></html>"

                status = 200
            elif value == "":
                try:
                    conn.request("GET", REQ_LINE)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")
                data1 = r1.read().decode()
                total_info = json.loads(data1)

                species_info = total_info['species']

                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT LIST</title>
                            </head>
                            <body style="background-color: lightblue;">
                                <p>The total number of species in the ensembl is: {len(species_info)}</p>
                                <p>The limit you have selected is: {value}</p>
                                <p>The name of the species are: </p>
                                <ol>  
                            """

                species_list = ""
                for i in range(len(species_info)):
                    species_list = species_list + "<li>"
                    species_list = species_list + species_info[i]['common_name']
                    species_list = species_list + "</li>"
                species_list = species_list + "</ol></body></html>"
                contents += f"<p>{species_list}</p>"
                contents += "</body></html>"

                status = 200
        elif verb == "/species":
            pair = arguments[1]
            msg, species = pair.split("=")
            REQ_LINE = ENDPOINT[1] + species + PARAMETERS
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

            species_list = ""
            for i in range(len(species_karyotype)):
                species_list = species_list + "<br>"
                species_list = species_list + species_karyotype[i]
            species_list = species_list + "</ol></body></html>"
            contents += f"<p>{species_list}</p>"
            contents += "</body></html>"

            status = 200
        else:
            contents = Path("Error.html").read_text()
            status = 404

        self.send_response(status)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()