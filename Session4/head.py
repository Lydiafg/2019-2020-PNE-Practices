from pathlib import Path
try:
    file_name = "RNU6-269P.txt"
    with open (file_name, "r") as f:
        file_contents = Path(file_name).read_text()
        header = next(f)
        f.close()
    print(header)
except FileNotFoundError:
            print("That filename does not exist")