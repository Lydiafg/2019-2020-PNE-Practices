from pathlib import Path

try:
    file_name = "ADA.txt"
    with open(file_name, "r") as f:
        file_contents = Path(file_name).read_text()
        components = file_contents.split("\n")[1:]
        body_file = ",".join(components).replace(",", "")
        print(len(body_file))
        f.close()
except FileNotFoundError:
    print("That filename does not exist")