from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    contents = Path(filename).read_text()
    body = contents.split("\n")[:1]
    return"".join(body)