import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

get_seq = ["ACCGT", "TACCG", "CGGTA", "GCCTA", "AAAGC"]

folder = "../Session4/"
format_ = ".txt"

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
            contents = Path("form-4.html").read_text()
            status = 200
        elif path == "/form-4.html":
            contents = Path("form-4.html").read_text()
            status = 200
        elif verb == "/":
            contents = Path('form-4.html').read_text()
            status = 200
        elif verb == "/ping":

            contents = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>PING OK!</title>
                        </head>
                        <body>
                        <h1>PING OK!</h1>
                        <h2>The Seq-2 Server is running...</h2>
                        <a href="form-4.html">Main page</a>
                        """
            status = 200
        elif verb == "/get":
            pair = arguments[1]
            pairs = pair.split('&')
            option, number = pairs[0].split('=')
            num = int(number)
            sequence = get_seq[num]
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>GET SEQUENCE</title>
                        </head>
                        <body>
                        <h2>Sequence number {num}</h2>
                        <p> {sequence} </p>
                        <a href="form-4.html">Main page</a>
                        </body>
                        </html>
                        """
            status = 200
        elif verb == "/gene":
            pair = arguments[1]
            pairs = pair.split('&')
            name, gene = pairs[0].split('=')
            seq = Seq()
            read_seq = seq.read_fasta(folder + gene + format_)
            contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>GET SEQUENCE</title>
                            </head>
                            <body>
                            <h2>Gene {gene}</h2>
                            <textarea readonly rows="20" cols="80"> {read_seq} </textarea>
                            <br>
                            <br>
                            <a href="form-4.html">Main page</a>
                            </body>
                            </html>
                            """
            status = 200
        elif verb == "/operation":
            pair = arguments[1]
            pairs = pair.split('&')
            msg, sequence = pairs[0].split('=')
            operation, name_ = pairs[1].split('=')
            name = str(name_)
            seq = Seq(sequence)
            if name == "Info":
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>INFO SEQUENCE</title>
                                </head>
                                <body>
                                <h1>Sequence</h1>
                                <p> {sequence}</p>
                                <h1>Operation:</h1>
                                <p>{name}</p>
                                <h1>Result:</h1>
                                <p>Total length: {seq.len()}</p>
                                <p>A:{seq.count_base("A")}</p>
                                <p>C:{seq.count_base("C")}</p>
                                <p>G:{seq.count_base("G")}</p>
                                <p>T:{seq.count_base("T")}</p>
                                <br>
                                <br>
                                <a href="form-4.html">Main page</a>
                                </body>
                                </html>
                                """
            elif name == "Comp":
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>INFO SEQUENCE</title>
                                </head>
                                <body>
                                <h1>Sequence</h1>
                                <h2> {sequence}</h2>
                                <h1>Operation:</h1>
                                <h2>{name}</h2>
                                <h1>Result:</h1>
                                <h2>{seq.complement()}</h2>
                                <br>
                                <br>
                                <a href="form-4.html">Main page</a>
                                </body>
                                </html>
                                """
            elif name == "Rev":
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>INFO SEQUENCE</title>
                                </head>
                                <body>
                                <h1>Sequence</h1>
                                <h2> {sequence}</h2>
                                <h1>Operation:</h1>
                                <h2>{name}</h2>
                                <h1>Result:</h1>
                                <h2>{seq.reverse()}</h2>
                                <br>
                                <br>
                                <a href="form-4.html">Main page</a>
                                </body>
                                </html>
                                """
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