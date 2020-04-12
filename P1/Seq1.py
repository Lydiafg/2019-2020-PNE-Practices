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