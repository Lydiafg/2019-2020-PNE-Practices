import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(' ')
        method = req_line[0]
        path = req_line[1]
        path = path[1:]
        contents = ""
        status = 0

        arguments = path.split('?')
        verb = arguments[0]

        if path == "":
            contents = Path("form-EX01.html").read_text()
            status = 200
            if verb == "/":
                contents = Path('form-EX01.html').read_text()
                status = 200
            elif verb == "/echo":
                pair = arguments[1]
                name, value = pair.split("=")
                contents = """
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT</title>
                            </head>
                            <body>
                            <h2>Received message:</h2>
                            """
                contents += f"<p>{value}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                status = 200

        elif path == "form-EX01.html":
            contents = Path("form-EX01.html").read_text()
            status = 200
            if verb == "/":
                contents = Path('form-EX01.html').read_text()
                status = 200
            elif verb == "/echo":
                pair = arguments[1]
                name, value = pair.split("=")
                contents = """
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT</title>
                            </head>
                            <body>
                            <h2>Received message:</h2>
                            """
                contents += f"<p>{value}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                status = 200
        else:
            contents = Path("Error.html").read_text()
            status = 404

        # Generating the response message
        self.send_response(status)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()