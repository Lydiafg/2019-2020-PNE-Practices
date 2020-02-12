from pathlib import Path
try:
    file_name = "U5.txt"
    with open (file_name, "r") as f:
        file_contents = Path(file_name).read_text()
        header = next(f)
        for line in f:
            components = line.replace("\n", "")
            print(components)
        f.close()
except FileNotFoundError:
            print("That filename does not exist")
