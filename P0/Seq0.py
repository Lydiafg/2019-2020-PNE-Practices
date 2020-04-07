from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    contents = Path(filename).read_text()
    body = contents.split("\n")[:1]
    return"".join(body)

def seq_len(filename):
    counter = 0
    for i in filename:
        counter = counter + 1
    return counter

def seq_count_base(seq, base):
    counter = 0
    for base in seq:
        counter = counter + 1
    return counter

def seq_count(seq):
    dictionary = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
           'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return dictionary

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    comp_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    new_seq = ""
    for base in seq:
        new_seq += comp_bases[base]
    return new_seq
