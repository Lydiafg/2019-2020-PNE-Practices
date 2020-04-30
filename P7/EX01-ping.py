import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = "/info/ping"
PARAMETERS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETERS

print(f"Server: {SERVER}")
print(f"URL : {URL}")


# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/info/ping" + "?content-type=application/json")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode()

# -- Create a variable with the data,
# -- form the JSON received
ping = json.loads(data1)


if ping['ping'] == 1:
    print("PING OK! The database is running!")
