from pathlib import Path


class Seq:
    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            self.strbases = "NULL"
            print("NULL sequence created")
            return
        if not self.valid_str(strbases):
            self.strbases = "Error"
            print("Not valid sequence")
            return
        self.strbases = strbases
        print("New sequence created")

    def __str__(self):
        return self.strbases

    @staticmethod
    def ping():
        print("PING OK")

    @staticmethod
    def valid_str(strbases):
        valid_bases = ['A', 'C', 'T', 'G']
        for b in strbases:
            if b not in valid_bases:
                return False
        return True

    def len(self):
        return len(self.strbases)

    def read_fasta(self, filename):
        contents = Path(filename).read_text()
        body = contents.split('\n')[1:]
        self.strbases = "".join(body)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        res = {'A': self.count_base('A'), 'T': self.count_base('T'),
               'C': self.count_base('C'), 'G': self.count_base('G')}
        return res

    def reverse(self):
        return self.strbases[::-1]

    def complement(self):
        basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        res = ""
        for b in self.strbases:
            res += basec[b]
        return res