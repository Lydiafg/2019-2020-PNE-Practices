class Seq:

    def __init__(self, strbases):
        bases = ["A", "C", "G", "T"]
        for i in strbases:
            if i not in bases:
                print("ERROR!")
                self.strbases = "ERROR"
            else:
                self.strbases = strbases
        print("New sequence created!")
        return

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)