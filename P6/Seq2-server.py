import http.server
import socketserver
import termcolor
from pathlib import Path


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
            contents = Path("form-1.html").read_text()
            status = 200
        elif path == "/form-1.html":
            contents = Path("form-1.html").read_text()
            status = 200
        elif verb == "/":
            contents = Path('form-1.html').read_text()
            status = 200
        elif verb == "/echo":
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
                        <a href="form-1.html">Main page</a>
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