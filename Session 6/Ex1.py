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


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("Hello? Am I a valid sequence?")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
