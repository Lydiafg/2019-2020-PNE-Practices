from pathlib import Path
class Seq:
    NULL = "NULL"

    def __init__(self, strbases=NULL):
        bases = ["A", "C", "G", "T"]
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL seq created")
        else:
            for i in strbases:
                if i not in bases:
                    print("INVALID!")
                    self.strbases = "ERROR"
                else:
                    self.strbases = strbases
            print("New sequence created!")
        return

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == self.NULL:
            return "0"
        elif self.strbases == "ERROR":
            return "0"
        else:
            return len(self.strbases)

    def count_base(self, seq):
        counter = 0
        if self.strbases == self.NULL:
            for base in seq:
                counter = 0
        elif self.strbases == "ERROR":
            for base in seq:
                counter = 0
        else:
            for base in seq:
                counter = counter + 1
        return counter

    def count(self):
        for base in ['A', 'C', 'T', 'G']:
            dictionary = {f" A : {self.count_base('A')}", f" C : {self.count_base('C')}", f" G : {self.count_base('G')}", f" T : {self.count_base('T')}"}
        return dictionary

    def reverse(self):
        if self.strbases == self.NULL:
            return self.strbases
        elif self.strbases == "ERROR":
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        comp_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        new_seq = ""
        if self.strbases == self.NULL:
            return self.strbases
        elif self.strbases == "ERROR":
            return self.strbases
        else:
            for base in self.strbases:
                new_seq += comp_bases[base]
            return new_seq

    def read_fasta(self, filename):
        contents = Path(filename).read_text()
        body = contents.split("\n")[1:]
        self.strbases = "".join(body)
        return self